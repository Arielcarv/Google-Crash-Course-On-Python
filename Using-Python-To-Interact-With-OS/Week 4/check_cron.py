import sys 
import re

logfile = sys.argv[1]

def get_cron_users_list():
    pattern = r"USER \((\w*)\)$"
    users_list = []
    with open(logfile) as log:
        for line in log:
            if "CRON" not in line:
                continue
            result = re.search(pattern, line)
            users_list.append(result[1])
    return users_list


def get_time_of_pid():
  pattern = r"^(.*)\scomputer.*\[(\d*)\]"
  pid_times = []
  with open(logfile) as log:
    for line in log:
        if "CRON" not in line:
            continue
        result = re.search(pattern, line)
        pid_times.append(f"{result[1]} pid:{result[2]}")
  return pid_times

print(get_cron_users_list())
print(get_time_of_pid())