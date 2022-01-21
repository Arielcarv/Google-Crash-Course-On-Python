import sys
import re

logfile = sys.argv[1]
usernames_dict = {}


def get_cron_users_list():
    usernames_dict = {}
    pattern = r"USER \((\w*)\)$"
    with open(logfile) as log:
        for line in log:
            result = re.search(pattern, line)
            if ("CRON" not in line) or (result is None):
                continue
            username = result.group(1)
            usernames_dict[username] = usernames_dict.get(username, 0) + 1
    return usernames_dict

print(get_cron_users_list())