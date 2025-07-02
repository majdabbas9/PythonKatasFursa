class URLShortener:
    """
    A URL Shortener is a service that converts a long URL into a shorter, more manageable URL.

    Your task is to implement a simple URL shortener system with the following features:

    - Convert a long URL into a short URL.
    - Retrieve the original long URL from a given short URL.
    - Assume there are NO hash collisions (i.e., each long URL maps to a unique short one).

    You can use base62 encoding logic using characters [A-Z, a-z, 0-9].
    You can use uuid for ID generation logic.
    """

    BASE_URL = "http://short.ly/"

    def __init__(self):
        """
        Initializes the URL shortener system with an internal mapping.
        """
        self.url_map = {}

    def shorten(self, long_url: str) -> str:
        """
        Shortens the provided long URL using base62 encoding.

        Args:
            long_url: The original long URL.

        Returns:
            A shortened URL string.
        """
        raise NotImplementedError("shorten() not implemented yet.")

    def retrieve(self, short_url: str) -> str | None:
        """
        Retrieves the original long URL from a given short URL.

        Args:
            short_url: The short URL string.

        Returns:
            The original long URL, or None if not found.
        """
        raise NotImplementedError("retrieve() not implemented yet.")


if __name__ == '__main__':
    shortener = URLShortener()

    long_url = "https://www.example.com/some/really/long/url"
    short_url = shortener.shorten(long_url)

    print("Shortened URL:", short_url)            # e.g. "http://short.ly/Xa9z"
    print("Original URL:", shortener.retrieve(short_url))  # "https://www.example.com/some/really/long/url"
