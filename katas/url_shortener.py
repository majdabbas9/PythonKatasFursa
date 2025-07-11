import uuid
import string
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
    CHARSET = string.ascii_letters + string.digits
    def __init__(self):
        """
        Initializes the URL shortener system with an internal mapping.
        """
        self.reverse_map = {}
        self.url_map = {}

    def _encode_base62(self, num: int) -> str:
        """
        Encodes an integer into a Base62 string.
        """
        if num == 0:
            return self.CHARSET[0]

        base62 = []
        while num > 0:
            num, rem = divmod(num, 62)
            base62.append(self.CHARSET[rem])
        return ''.join(reversed(base62))

    def shorten(self, long_url: str) -> str:
        """
        Shortens the provided long URL using base62 encoding.

        Args:
            long_url: The original long URL.

        Returns:
            A shortened URL string.
        """
        if long_url in self.reverse_map:
            short_code = self.reverse_map[long_url]
        else:
            # Generate a unique ID and encode it
            unique_id = uuid.uuid4().int >> 64  # Use top 64 bits for a shorter ID
            short_code = self._encode_base62(unique_id)

            # Save mappings
            self.url_map[short_code] = long_url
            self.reverse_map[long_url] = short_code

        return self.BASE_URL + short_code

    def retrieve(self, short_url: str) -> str | None:
        """
        Retrieves the original long URL from a given short URL.

        Args:
            short_url: The short URL string.

        Returns:
            The original long URL, or None if not found.
        """
        if not short_url.startswith(self.BASE_URL):
            return None
        short_code = short_url[len(self.BASE_URL):]
        return self.url_map.get(short_code)


if __name__ == '__main__':
    shortener = URLShortener()

    long_url = "https://www.example.com/some/really/long/url"
    short_url = shortener.shorten(long_url)

    print("Shortened URL:", short_url)  # e.g. "http://short.ly/Xa9z"
    print("Original URL:", shortener.retrieve(short_url))  # "https://www.example.com/some/really/long/url"
