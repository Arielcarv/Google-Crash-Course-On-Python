#!/usr/bin/env python3
'''
Before you dig into Exercise 3, run this command in the shell
(not in python):
sudo apt-get install apache2 -y
 
When calling ticky_check, the  filepath has to be passed.
Mine looked like this:
./ticky_check.py /home/student-01-a297e7359c16/syslog.log
 
Remember to chmod +x the script after you save it (and before 
you execute it).
 
Also, at the end of Ex. 3, name html files as
error_message.html   and    user_statistics.html
 
sudo chmod +x csv_to_html.py  (done already)
 
'''

import sys
import re
import csv
import itertools
import operator


def statistics(logfile):

  per_user = {}
  error = {}

  with open(logfile, "r") as file:
    for line in file.readlines():
      pattern = r": ([A-Z]*) ([\w ']*) [\[\]\d# ]*\(([\w\.]*)\)$"
      message = re.search(pattern, line)
      log_type = message.group(1)
      log_message = message.group(2)
      user = message.group(3)
      log_user = (user[1:-1]).capitalize()
      # Error count
      if log_type == "ERROR":
        if log_message not in error:
          error[log_message] = 0
        error[log_message] += 1
      # User stats
      if log_user not in per_user:
          per_user[log_user] = {"ERROR": 0, "INFO": 0}
      if log_type == "ERROR":
          per_user[log_user]["ERROR"] += 1
      elif log_type == "INFO":
          per_user[log_user]["INFO"] += 1

  # Sorting the dictionaries:
  per_user = {k: v for k, v in sorted(per_user.items())}
  error = {k: v for k, v in sorted(error.items(), key=lambda v: v[1], reverse=True)}

  return per_user, error


def to_csv(per_user, error):
    with open("user_statistics.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Username", "Error", "Info"])
        dU = per_user
        for line in dU:
            for key in dU:
                writer.writerow([key, dU[key]["ERROR"], dU[key]["INFO"]])
    with open("error_message.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Error", "Count"])
        dE = error
        for line in dE:
            for key in dE:
                writer.writerow([key, "Count"])


if __name__ == "__main__":
  logfile = sys.argv[1]
  per_user, error = statistics(logfile)
  to_csv(per_user, error)
