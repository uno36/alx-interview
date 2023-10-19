#!/usr/bin/python3
"""0-stats module
"""
import sys


stats = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total = 0
count = 0


def print_stats(stats, total):
    """print_stats function
    """
    print("File size: {}".format(total))
    for key, value in sorted(stats.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            data = line.split()
            if len(data) > 4:
                status = data[-2]
                if status in stats.keys():
                    stats[status] += 1
                total += int(data[-1])
                count += 1
            if count == 10:
                count = 0
                print_stats(stats, total)
    except Exception:
        pass
    finally:
        print_stats(stats, total)
