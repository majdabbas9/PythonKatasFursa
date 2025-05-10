import unittest
from typing import Dict
from katas.nginx_log_parser import parse_log  # replace with the actual import

class TestParseLog(unittest.TestCase):

    def test1(self):
        log = '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] "GET /test.js HTTP/1.1" 200 1684 "-" "Opera/9.58"'
        expected = {
            "client_ip": "122.176.223.47",
            "date": "05/Feb/2024:08:29:40 +0000",
            "http_method": "GET",
            "path": "/test.js",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "1684",
            "user_agent": "Opera/9.58"
        }
        self.assertEqual(parse_log(log), expected)

    def test2(self):
        log = '10.0.0.1 - - [01/Jan/2025:12:00:00 +0000] "POST /login HTTP/1.0" 404 512 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "10.0.0.1",
            "date": "01/Jan/2025:12:00:00 +0000",
            "http_method": "POST",
            "path": "/login",
            "http_version": "1.0",
            "status": "404",
            "response_bytes": "512",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test3(self):
        log = '192.168.1.1 - - [15/Mar/2023:10:10:10 +0000] "PUT /api/data HTTP/2.0" 201 1024 "-" "curl/7.64.1"'
        expected = {
            "client_ip": "192.168.1.1",
            "date": "15/Mar/2023:10:10:10 +0000",
            "http_method": "PUT",
            "path": "/api/data",
            "http_version": "2.0",
            "status": "201",
            "response_bytes": "1024",
            "user_agent": "curl/7.64.1"
        }
        self.assertEqual(parse_log(log), expected)

    def test4(self):
        log = '8.8.8.8 - - [20/Apr/2024:15:20:30 +0000] "HEAD /check HTTP/1.1" 200 0 "-" "Mozilla/4.0"'
        expected = {
            "client_ip": "8.8.8.8",
            "date": "20/Apr/2024:15:20:30 +0000",
            "http_method": "HEAD",
            "path": "/check",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "0",
            "user_agent": "Mozilla/4.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test5(self):
        log = '203.0.113.5 - - [22/Nov/2023:09:05:15 +0000] "GET /home HTTP/1.1" 301 523 "-" "Chrome/91.0"'
        expected = {
            "client_ip": "203.0.113.5",
            "date": "22/Nov/2023:09:05:15 +0000",
            "http_method": "GET",
            "path": "/home",
            "http_version": "1.1",
            "status": "301",
            "response_bytes": "523",
            "user_agent": "Chrome/91.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test6(self):
        log = '192.168.0.100 - - [30/Dec/2022:18:59:59 +0000] "POST /submit HTTP/1.1" 500 1024 "-" "Safari/13.1"'
        expected = {
            "client_ip": "192.168.0.100",
            "date": "30/Dec/2022:18:59:59 +0000",
            "http_method": "POST",
            "path": "/submit",
            "http_version": "1.1",
            "status": "500",
            "response_bytes": "1024",
            "user_agent": "Safari/13.1"
        }
        self.assertEqual(parse_log(log), expected)

    def test7(self):
        log = '172.16.0.5 - - [11/Feb/2024:10:30:20 +0000] "DELETE /files HTTP/2.0" 200 1200 "-" "PostmanRuntime/7.26.10"'
        expected = {
            "client_ip": "172.16.0.5",
            "date": "11/Feb/2024:10:30:20 +0000",
            "http_method": "DELETE",
            "path": "/files",
            "http_version": "2.0",
            "status": "200",
            "response_bytes": "1200",
            "user_agent": "PostmanRuntime/7.26.10"
        }
        self.assertEqual(parse_log(log), expected)

    def test8(self):
        log = '203.0.113.7 - - [03/Jan/2023:12:10:00 +0000] "PATCH /update HTTP/1.1" 404 999 "-" "curl/7.58.0"'
        expected = {
            "client_ip": "203.0.113.7",
            "date": "03/Jan/2023:12:10:00 +0000",
            "http_method": "PATCH",
            "path": "/update",
            "http_version": "1.1",
            "status": "404",
            "response_bytes": "999",
            "user_agent": "curl/7.58.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test9(self):
        log = '192.168.100.1 - - [04/Feb/2024:15:00:00 +0000] "GET /index.html HTTP/1.1" 200 2048 "-" "Firefox/98.0"'
        expected = {
            "client_ip": "192.168.100.1",
            "date": "04/Feb/2024:15:00:00 +0000",
            "http_method": "GET",
            "path": "/index.html",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "2048",
            "user_agent": "Firefox/98.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test10(self):
        log = '192.0.2.1 - - [10/Apr/2024:09:10:10 +0000] "GET /about HTTP/1.1" 301 301 "-" "Edge/92.0"'
        expected = {
            "client_ip": "192.0.2.1",
            "date": "10/Apr/2024:09:10:10 +0000",
            "http_method": "GET",
            "path": "/about",
            "http_version": "1.1",
            "status": "301",
            "response_bytes": "301",
            "user_agent": "Edge/92.0"
        }
        self.assertEqual(parse_log(log), expected)

    # Add more test cases to test variations (valid and invalid logs), e.g.:

    def test11(self):
        log = '203.0.113.9 - - [02/Mar/2024:11:10:00 +0000] "GET /dashboard HTTP/1.1" 403 0 "-" "Chrome/90.0"'
        expected = {
            "client_ip": "203.0.113.9",
            "date": "02/Mar/2024:11:10:00 +0000",
            "http_method": "GET",
            "path": "/dashboard",
            "http_version": "1.1",
            "status": "403",
            "response_bytes": "0",
            "user_agent": "Chrome/90.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test12(self):
        log = '198.51.100.1 - - [22/Mar/2024:14:30:00 +0000] "GET /api HTTP/1.1" 404 256 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "198.51.100.1",
            "date": "22/Mar/2024:14:30:00 +0000",
            "http_method": "GET",
            "path": "/api",
            "http_version": "1.1",
            "status": "404",
            "response_bytes": "256",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test13(self):
        log = '192.0.2.3 - - [31/Dec/2023:23:59:59 +0000] "GET /large-file.zip HTTP/1.1" 200 9999999 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"'
        expected = {
            "client_ip": "192.0.2.3",
            "date": "31/Dec/2023:23:59:59 +0000",
            "http_method": "GET",
            "path": "/large-file.zip",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "9999999",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.assertEqual(parse_log(log), expected)

    def test14(self):
        log = '203.0.113.11 - - [01/Jan/2025:00:00:00 +0000] "PUT /update-info HTTP/1.1" 500 1024 "-" ""'
        expected = {
            "client_ip": "203.0.113.11",
            "date": "01/Jan/2025:00:00:00 +0000",
            "http_method": "PUT",
            "path": "/update-info",
            "http_version": "1.1",
            "status": "500",
            "response_bytes": "1024",
            "user_agent": ""
        }
        self.assertEqual(parse_log(log), expected)

    def test15(self):
        log = '192.168.0.1 - - [05/Feb/2024:17:35:20 +0000] "GET /special-chars/%20%23%24%25 HTTP/2.0" 301 250 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "192.168.0.1",
            "date": "05/Feb/2024:17:35:20 +0000",
            "http_method": "GET",
            "path": "/special-chars/%20%23%24%25",
            "http_version": "2.0",
            "status": "301",
            "response_bytes": "250",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test16(self):
        log = '203.0.113.15 - - [06/Mar/2023:09:22:10 +0000] "GET /hello/world HTTP/1.0" 404 150 "-" "Windows NT 6.1; WOW64; rv:40.0"'
        expected = {
            "client_ip": "203.0.113.15",
            "date": "06/Mar/2023:09:22:10 +0000",
            "http_method": "GET",
            "path": "/hello/world",
            "http_version": "1.0",
            "status": "404",
            "response_bytes": "150",
            "user_agent": "Windows NT 6.1; WOW64; rv:40.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test17(self):
        log = '2001:0db8:85a3:0000:0000:8a2e:0370:7334 - - [10/Apr/2024:22:15:00 +0000] "POST /contact HTTP/1.1" 200 500 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "date": "10/Apr/2024:22:15:00 +0000",
            "http_method": "POST",
            "path": "/contact",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "500",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test18(self):
        log = '127.0.0.1 - - [01/Jan/2023:10:00:00 +0000] "GET /favicon.ico HTTP/1.1" 404 0 "-" "curl/7.58.0"'
        expected = {
            "client_ip": "127.0.0.1",
            "date": "01/Jan/2023:10:00:00 +0000",
            "http_method": "GET",
            "path": "/favicon.ico",
            "http_version": "1.1",
            "status": "404",
            "response_bytes": "0",
            "user_agent": "curl/7.58.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test19(self):
        log = '10.10.10.10 - - [12/Nov/2024:07:20:30 +0000] "GET /big-data/file1234567890.pdf HTTP/2.0" 200 20000 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"'
        expected = {
            "client_ip": "10.10.10.10",
            "date": "12/Nov/2024:07:20:30 +0000",
            "http_method": "GET",
            "path": "/big-data/file1234567890.pdf",
            "http_version": "2.0",
            "status": "200",
            "response_bytes": "20000",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
        self.assertEqual(parse_log(log), expected)

    def test20(self):
        log = '172.16.254.1 - - [29/Feb/2024:12:45:10 +0000] "GET /nonexistent HTTP/1.1" 404 404 "-" "Opera/9.80"'
        expected = {
            "client_ip": "172.16.254.1",
            "date": "29/Feb/2024:12:45:10 +0000",
            "http_method": "GET",
            "path": "/nonexistent",
            "http_version": "1.1",
            "status": "404",
            "response_bytes": "404",
            "user_agent": "Opera/9.80"
        }
        self.assertEqual(parse_log(log), expected)

    def test21(self):
        log = '172.25.0.5 - - [31/Dec/2024:00:00:00 +0000] "GET /hello-world HTTP/1.0" 200 1000 "-" "Googlebot/2.1"'
        expected = {
            "client_ip": "172.25.0.5",
            "date": "31/Dec/2024:00:00:00 +0000",
            "http_method": "GET",
            "path": "/hello-world",
            "http_version": "1.0",
            "status": "200",
            "response_bytes": "1000",
            "user_agent": "Googlebot/2.1"
        }
        self.assertEqual(parse_log(log), expected)

    def test22(self):
        log = 'INVALID LOG ENTRY WITH RANDOM DATA'
        with self.assertRaises(ValueError):
            parse_log(log)

    def test23(self):
        log = '::1 - - [01/Jun/2023:16:30:00 +0000] "GET /ip-version HTTP/1.1" 200 300 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "::1",
            "date": "01/Jun/2023:16:30:00 +0000",
            "http_method": "GET",
            "path": "/ip-version",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "300",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test24(self):
        log = '203.0.113.10 - - [20/Apr/2025:19:55:00 +0000] "GET /api/data HTTP/1.0" 400 - "-" "curl/7.64.1"'
        expected = {
            "client_ip": "203.0.113.10",
            "date": "20/Apr/2025:19:55:00 +0000",
            "http_method": "GET",
            "path": "/api/data",
            "http_version": "1.0",
            "status": "400",
            "response_bytes": "-",
            "user_agent": "curl/7.64.1"
        }
        self.assertEqual(parse_log(log), expected)

    def test25(self):
        log = '198.51.100.20 - - [05/May/2024:05:10:10 +0000] "GET / HTTP/2.0" 200 12345 "-" "Safari/13.1"'
        expected = {
            "client_ip": "198.51.100.20",
            "date": "05/May/2024:05:10:10 +0000",
            "http_method": "GET",
            "path": "/",
            "http_version": "2.0",
            "status": "200",
            "response_bytes": "12345",
            "user_agent": "Safari/13.1"
        }
        self.assertEqual(parse_log(log), expected)

    def test26(self):
        log = '::1 - - [01/Jun/2023:16:30:00 +0000] "GET /ip-version HTTP/1.1" 200 300 "-" "Mozilla/5.0"'
        expected = {
            "client_ip": "::1",
            "date": "01/Jun/2023:16:30:00 +0000",
            "http_method": "GET",
            "path": "/ip-version",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "300",
            "user_agent": "Mozilla/5.0"
        }
        self.assertEqual(parse_log(log), expected)

    def test27(self):
        log = '10.0.0.1 - - [14/Feb/2024:12:00:00 +0000] "GET /upload?file=bigfile HTTP/1.1" 200 1048576 "-" "wget/1.20"'
        expected = {
            "client_ip": "10.0.0.1",
            "date": "14/Feb/2024:12:00:00 +0000",
            "http_method": "GET",
            "path": "/upload?file=bigfile",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "1048576",
            "user_agent": "wget/1.20"
        }
        self.assertEqual(parse_log(log), expected)
    # And continue adding test cases up to test30.

