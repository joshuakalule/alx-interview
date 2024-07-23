#!/usr/bin/env python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import re

params = {
    "file_size": 0,
    "code_map": {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    },
}

# generate regex
ip = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
date = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
time = r"[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}"
uri = r"GET /projects/260 HTTP/1\.1"
code = "|".join([s for s in params["code_map"].keys()])
size = r"\d*"

regex = r"{} - \[{} {}\] \"{}\" ({}) ({})".format(
    ip, date, time, uri, code, size
    )


def print_stats(**kwargs):
    print(f"File size: {kwargs['file_size']}")
    for code, count in kwargs["code_map"].items():
        print(f"{code}: {count}")


if __name__ == "__main__":

    n = 0
    try:
        for line in sys.stdin:
            # increment n
            n += 1
            # routine check
            if n == 10:
                n = 0
                print_stats(**params)

            # process line
            if not (m:=re.search(regex, line)):
                continue

            status_code = m.group(1)
            file_size = int(m.group(2))

            params['code_map'][status_code] += 1
            params["file_size"] += file_size
    except KeyboardInterrupt:
        print_stats(**params)
        raise
