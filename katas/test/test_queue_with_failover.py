import unittest
import time
from katas.queue_with_failover import QueueWithFailover, EmptyQueueException  # Adjust as needed


class TestQueueWithFailover(unittest.TestCase):

    def test_send_and_size(self):
        """Ensure sending jobs increments visible size correctly."""
        q = QueueWithFailover(2)
        q.send_job("A")
        q.send_job("B")
        self.assertEqual(q.size(), 2)

    def test_get_and_in_flight_size(self):
        """Getting a job should decrease visible and increase in-flight."""
        q = QueueWithFailover(2)
        q.send_job("Job1")
        job = q.get_job()
        self.assertEqual(job, "Job1")
        self.assertEqual(q.size(), 0)
        self.assertEqual(q.in_flight_size(), 1)

    def test_job_done_removes_from_in_flight(self):
        """Completing a job removes it from hidden jobs."""
        q = QueueWithFailover(2)
        q.send_job("DoneJob")
        job = q.get_job()
        q.job_done(job)
        self.assertEqual(q.in_flight_size(), 0)

    def test_job_done_on_expired_job_raises(self):
        """Trying to complete an expired job should raise error."""
        q = QueueWithFailover(1)
        q.send_job("LateJob")
        job = q.get_job()
        time.sleep(1.2)
        q.return_expired_jobs_to_queue()
        with self.assertRaises(ValueError):
            q.job_done(job)

    def test_return_expired_job_to_queue(self):
        """Expired job should be moved back to visible queue."""
        q = QueueWithFailover(1)
        q.send_job("FailoverJob")
        job = q.get_job()
        time.sleep(1.1)
        q.return_expired_jobs_to_queue()
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.in_flight_size(), 0)
        self.assertEqual(q.get_job(), "FailoverJob")

    def test_get_job_empty_raises(self):
        """Getting from empty queue raises exception."""
        q = QueueWithFailover(2)
        with self.assertRaises(EmptyQueueException):
            q.get_job()

    def test_send_non_string_raises(self):
        """Sending a non-string job should raise TypeError."""
        q = QueueWithFailover(2)
        with self.assertRaises(TypeError):
            q.send_job(123)

    def test_job_done_not_in_hidden_raises(self):
        """Calling job_done on unseen job should raise ValueError."""
        q = QueueWithFailover(2)
        q.send_job("ghost")
        with self.assertRaises(ValueError):
            q.job_done("ghost")

    def test_is_empty_true_on_init(self):
        """Queue should be empty initially."""
        q = QueueWithFailover(2)
        self.assertTrue(q.is_empty())

    def test_is_empty_false_after_send(self):
        """Queue should not be empty after sending a job."""
        q = QueueWithFailover(2)
        q.send_job("X")
        self.assertFalse(q.is_empty())


if __name__ == '__main__':
    unittest.main()
