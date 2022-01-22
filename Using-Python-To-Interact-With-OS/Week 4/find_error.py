#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            print(f"LOG: {log}")
            error_patterns = []
            for error_index in error.split(" "):
                # print(f"ERROR INDEX: {error_index}")
                error_patterns.append(r"{}".format(error_index.lower()))
            print(f"ERROR PATTERNS: {error_patterns}")
            for error_pattern in error_patterns:
                print(f"ERROR PATTERN: {error_pattern}")
                print(f"LOG LOWER: {log.lower()}")
                result = re.search(error_pattern, log.lower())
                print(result)
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors):
    # with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    with open('./errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
