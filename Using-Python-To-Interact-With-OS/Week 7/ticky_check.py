#!/usr/bin/env python3

import re
import sys
import csv
import operator

def generate_data_dictionaries(log_file_address):
	errors_dictionary = {}
	user_data_dictionary = {}

	with open(log_file_address, "r") as log_file:
		for line in log_file.readlines():
			#print(line)
			log_pattern = r": ([A-Z]*) ([A-Z]{1}.*) \((\S*)\)$"
			search = re.search(log_pattern, line)
			log_type = search.group(1)
			log_message = search.group(2)
			log_user = search.group(3)
			# Log message errors count
			if log_type == "ERROR":
				if log_message not in errors_dictionary:
					errors_dictionary[log_message] = 0
				errors_dictionary[log_message] += 1

			# User data
			if log_user not in user_data_dictionary:
				user_data_dictionary[log_user] = {"ERROR": 0,"INFO": 0}
			if log_type == "INFO": 
				user_data_dictionary[log_user]["INFO"] += 1
			if log_type == "ERROR":
				user_data_dictionary[log_user]["ERROR"] += 1

	user_data_dictionary = sorted(user_data_dictionary.items())
	errors_dictionary = sorted(errors_dictionary.items(), key=operator.itemgetter(1), reverse=True)
	return errors_dictionary, user_data_dictionary

def dictionaries_to_csv(errors_dictionary, user_data_dictionary):
	print(errors_dictionary, "\n")
	print(user_data_dictionary, "\n")

	with open("./error_message.csv", "w") as error_message_csv:
		writer = csv.writer(error_message_csv)
		writer.writerow(["Error", "Count"])
		writer.writerows(errors_dictionary)
	
	with open("./user_statistics.csv", "w") as user_statistics_csv:
		writer = csv.writer(user_statistics_csv)
		writer.writerow(["Username", "INFO", "ERROR"])
		for row in user_data_dictionary:
			print(row)
			username, log_types = row
			info_log = log_types["INFO"]
			error_log = log_types["ERROR"]
			print(username, info_log, error_log)
			writer.writerow([username, info_log, error_log])

if __name__ == "__main__":
	log_file_address = sys.argv[1]
	errors_dictionary, user_data_dictionary = generate_data_dictionaries(log_file_address)
	# print(dict(errors_dictionary), "\n")
	# print(dict(user_data_dictionary["username"]))
	dictionaries_to_csv(errors_dictionary, user_data_dictionary)
