import time


class EmptyQueueException(Exception):
    """
    Exception raised when attempting to get a job from an empty queue.
    """
    pass


class QueueWithFailover:
    """
    A job queue data structure with failover support.

    A job queue is a messaging system used to manage the flow of work between components or applications.
    In this system, jobs (or messages) are sent to the queue by PRODUCERS and retrieved by CONSUMERS for processing.

    When a job is consumed by a consumer, they have `job_timeout` seconds to finish the job.
    The job is not permanently deleted from the queue; instead, it is temporarily hidden.
    If the consumer completes processing the job within the allocated time, they mark the job as done (job_done()),
    and the job should be permanently deleted.
    Otherwise, if they fail to process the job and the job processing times out, the job should be returned
    to the end of the queue (by return_expired_jobs_to_queue()), allowing it to be consumed again.
    """

    def __init__(self, job_timeout):
        """
        Initialize an empty job queue.

        Args:
            job_timeout: Number of seconds a job is hidden before failing over.
        """
        self.job_timeout = job_timeout
        self.visible_jobs = []  # List of jobs that are visible in the queue
        self.hidden_jobs = {}  # Dictionary to store hidden jobs with their timestamps
        pass

    def is_empty(self):
        """
        Check if the job queue is empty.

        Returns:
            bool: True if the job queue is empty, False otherwise.
        """
        return len(self.visible_jobs) == 0 and len(self.hidden_jobs) == 0

    def send_job(self, job):
        """
        Send a job to the job queue.

        Args:
            job: The job (string) to be added to the queue.
        """
        if not isinstance(job, str):
            raise TypeError("Job must be a string.")
        self.visible_jobs.append(job)

    def get_job(self):
        """
        Retrieve and return a job from the front of the job queue.

        Returns:
            str: The job at the front of the queue.

        Raises:
            EmptyQueueException: If the job queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("The job queue is empty.")
        job = self.visible_jobs.pop()
        self.hidden_jobs[job] = time.time()  # Store the job with the current timestamp
        return job

    def job_done(self, job):
        """
        Called when a consumer completes a consumed job.

        The job should be deleted permanently from the hidden jobs.

        Args:
            job: The job string to be marked as done.

        Raises:
            ValueError: If the job is not found in the hidden jobs.
        """
        if not isinstance(job, str):
            raise TypeError("Job must be a string.")
        current_time = time.time()
        if job not in self.hidden_jobs:
            raise ValueError("Job not found in hidden jobs.")
        if current_time - self.hidden_jobs.get(job) > self.job_timeout:
            self.visible_jobs.append(job)
            raise ValueError("Job has expired and cannot be marked as done.")
        else :
            del self.hidden_jobs[job]

    def size(self):
        """
        Return the number of jobs in the visible queue.

        Returns:
            int: Number of visible jobs.
        """
        return len(self.visible_jobs)


    def in_flight_size(self):
        """
        Return the number of hidden jobs (in-flight).

        Returns:
            int: Number of hidden jobs.
        """
        return len(self.hidden_jobs)

    def return_expired_jobs_to_queue(self):
        """
        Return hidden jobs that were retrieved more than `job_timeout` seconds ago
        back to the end of the visible queue.
        """
        current_time = time.time()
        expired_jobs = [job for job, timestamp in self.hidden_jobs.items()
                        if current_time - timestamp > self.job_timeout]
        for job in expired_jobs:
            self.visible_jobs.append(job)
            del self.hidden_jobs[job]


if __name__ == '__main__':
    job_queue = QueueWithFailover(3)

    job_queue.send_job("Job 1")
    job_queue.send_job("Job 2")
    job_queue.send_job("Job 3")

    print("Job Queue Size:", job_queue.size())

    current_job = job_queue.get_job()
    job_queue.job_done(current_job)

    current_job = job_queue.get_job()
    time.sleep(4)
    job_queue.return_expired_jobs_to_queue()

    try:
        job_queue.job_done(current_job)
    except ValueError:
        print("Job not found as it was expired and returned to the main queue")
