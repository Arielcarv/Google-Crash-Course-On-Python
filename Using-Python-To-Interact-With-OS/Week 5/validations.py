#!/usr/bin/env pyhton3

def validate_user(username, min_value):
	assert type(username) == str, "username must be a string"
	if min_value < 1:
		raise ValueError("minimum length must be at least 1")
	if len(username) < min_value:
		return False
	if not username.isalnum():
		return False
	return True