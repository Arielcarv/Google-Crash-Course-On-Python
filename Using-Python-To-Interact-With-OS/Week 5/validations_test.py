#!/usr/bin/env python3
from multiprocessing.sharedctypes import Value
import unittest

from validations import validate_user

class TestValidate(unittest.TestCase):
	def test_valid(self):
		self.assertEqual(validate_user("validUser", 3), True)

	def test_too_short(self):
		self.assertEqual(validate_user("inv", 5), False)

	def test_invalid_character(self):
		self.assertEqual(validate_user("invalid_user", 1), False)

	def test_invalid_minimum(self):
		self.assertRaises(ValueError, validate_user, "user", -1) # assertRaises(Error, function_name, parameter1, parameter2)

# Run tests
unittest.main()
