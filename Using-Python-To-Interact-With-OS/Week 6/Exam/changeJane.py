#!/usr/bin/env python3

import sys
import subprocess

with open("./oldFiles.txt", "r") as oldFiles:
	for line in oldFiles.readlines():
		old_name = line.strip()
		new_name = old_name.replace("jane", "jdoe")
		subprocess.run(["mv", old_name, new_name])