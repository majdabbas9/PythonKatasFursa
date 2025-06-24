import requests
from datetime import datetime
from typing import List


class GitHubRepoActivityIntensity:
    """
    Analyze the activity level of a specific GitHub repository.

    This class provides methods to:
    - Fetch commit timestamps for a given repository (including pagination).
    - Calculate the average time (in hours) between consecutive commits.

    Uses the GitHub REST API:
    GET https://api.github.com/repos/{owner}/{repo}/commits
    """

    GITHUB_API_BASE_URL = "https://api.github.com/repos"

    @staticmethod
    def fetch_commit_timestamps(owner: str, repo: str) -> List[datetime]:
        """
        Fetch commit timestamps for the specified repository using the GitHub API.

        Args:
            owner: The owner of the repository.
            repo: The name of the repository.

        Returns:
            A list of commit timestamps as datetime objects.

        Raises:
            Exception: If there is an error fetching or parsing the data.
        """
        raise NotImplementedError("Not implemented yet.")

    @staticmethod
    def calculate_average_time_between_commits(timestamps: List[datetime]) -> float:
        """
        Calculates the average time between consecutive commits.

        Args:
            timestamps: A list of commit timestamps.

        Returns:
            The average time between commits in hours.
        """
        raise NotImplementedError("Not implemented yet.")


if __name__ == '__main__':
    try:
        timestamps = GitHubRepoActivityIntensity.fetch_commit_timestamps("torvalds", "linux")
        avg_time = GitHubRepoActivityIntensity.calculate_average_time_between_commits(timestamps)
        print(f"The average time between commits in the repository is {avg_time:.2f} hours.")
    except Exception as e:
        print("Error:", str(e))
