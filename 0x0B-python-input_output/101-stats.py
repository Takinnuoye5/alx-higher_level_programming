#!/usr/bin/python3ads from standard input and computes metrics.

"""
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
   import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        _, _, _, status_code, file_size = line.strip().split(" ")
        status_code = int(status_code)
        file_size = int(file_size)
        status_codes[status_code] += 1
        total_size += file_size
        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for status_code in sorted(status_codes):
                if status_codes[status_code] != 0:
                    print(f"{status_code}: {status_codes[status_code]}")
except KeyboardInterrupt:
    print("Statistics since the beginning:")
    print("Total file size: ", total_size)
    for status_code in sorted(status_codes):
        if status_codes[status_code] != 0:
            print(f"{status_code}: {status_codes[status_code]}")
