import unittest
from urllib.parse import urlparse
from katas.url_shortener import URLShortener


class TestURLShortener(unittest.TestCase):

    def setUp(self):
        self.shortener = URLShortener()

    def test_1(self):
        long_url = "https://example.com/page"
        short_url = self.shortener.shorten(long_url)
        self.assertTrue(short_url.startswith(URLShortener.BASE_URL))

    def test_2(self):
        long_url = "https://example.com/a"
        short_url = self.shortener.shorten(long_url)
        self.assertEqual(self.shortener.retrieve(short_url), long_url)

    def test_3(self):
        long_url = "https://example.com/b"
        short1 = self.shortener.shorten(long_url)
        short2 = self.shortener.shorten(long_url)
        self.assertEqual(short1, short2)

    def test_4(self):
        url1 = "https://site1.com"
        url2 = "https://site2.com"
        s1 = self.shortener.shorten(url1)
        s2 = self.shortener.shorten(url2)
        self.assertNotEqual(s1, s2)

    def test_5(self):
        self.assertIsNone(self.shortener.retrieve("http://short.ly/invalid"))

    def test_6(self):
        self.assertIsNone(self.shortener.retrieve("http://wrongdomain.com/abc123"))

    def test_7(self):
        long_url = "https://newsite.com/data"
        short_url = self.shortener.shorten(long_url)
        code = short_url.split("/")[-1]
        self.assertTrue(code.isalnum())

    def test_8(self):
        long_url = "https://example.com/deep/link/structure"
        short_url = self.shortener.shorten(long_url)
        self.assertLess(len(short_url), len(long_url))

    def test_9(self):
        for i in range(100):
            url = f"https://bulk.com/item/{i}"
            short = self.shortener.shorten(url)
            self.assertEqual(self.shortener.retrieve(short), url)

    def test_10(self):
        url = "https://repeat.com"
        self.shortener.shorten(url)
        self.shortener.shorten(url)
        self.assertEqual(len(self.shortener.url_map), 1)
        self.assertEqual(len(self.shortener.reverse_map), 1)


if __name__ == '__main__':
    unittest.main()
