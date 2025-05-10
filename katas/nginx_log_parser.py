from typing import Dict
import re

def parse_log(log: str) -> Dict[str, str]:
    """
    Parses a single Nginx access log entry into a structured dictionary.

    The log format is:
    122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] "GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 "-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"

    The parsed log data should be returned as a dictionary:
    {
        "client_ip": "122.176.223.47",
        "date": "05/Feb/2024:08:29:40 +0000",
        "http_method": "GET",
        "path": "/web-enabled/Enhanced-portal/bifurcated-forecast.js",
        "http_version": "1.1",
        "status": "200",
        "response_bytes": "1684",
        "user_agent": "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"
    }

    Hint: Use regex

    Args:
        log: the Nginx log string

    Returns:
        A dictionary containing parsed log data

    Raises:
        ValueError: if the log format is invalid
    """
    client_ip_4 = re.search(r"([0-9]{1,3}\.){3}([0-9]{1,3})", log)
    client_ip_6 = re.search(r"([0-9a-fA-F:]{2,39})", log)
    date = re.search(r"[0-9]{2}/[a-z|A-Z]{0,3}/[0-9]{4}:([0-9]{2}:){2}[0-9]{2} \+[0-9]{4}",log)
    the_request = re.search(r"\"([a-z|A-Z]{,7})\s+(/[^ ]+|/)\s+(HTTP)/(\d+.\d+)\"\s+(\d+)\s+(\d+|-)",log)
    user_agent_search = re.search(r"(\"-\")\s+\"(.*)\"",log)
    if not date or not the_request or not user_agent_search or (not client_ip_4 and not client_ip_6):
        raise ValueError
    returned_file = {
        "client_ip": client_ip_4.group() if client_ip_4 else client_ip_6.group(),
        "date": date.group(),
        "http_method": the_request.groups()[0],
        "path": the_request.groups()[1],
        "http_version": the_request.groups()[3],
        "status": the_request.groups()[4],
        "response_bytes": the_request.groups()[5],
        "user_agent": user_agent_search.groups()[1]
    }
    return returned_file


if __name__ == "__main__":
    log_entry = (
        '198.51.100.20 - - [05/May/2024:05:10:10 +0000] "GET / HTTP/2.0" 200 12345 "-" "Safari/13.1"'
    )
    parsed_log = parse_log(log_entry)
    print("Parsed log data:", parsed_log)
