#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
	def test_basic_case(self):
		test_case = "Lovelace, Ada"
		expected = "Ada Lovelace"
		self.assertEqual(rearrange_name(test_case), expected)

	def test_empty(self):
		test_case = ""
		expected = ""
		self.assertEqual(rearrange_name(test_case), expected)

	def test_double_name(self):
		test_case = "Hopper, Grace M."
		expected = "Grace M. Hopper"
		self.assertEqual(rearrange_name(test_case), expected)

	def test_one_name(self):
		test_case = "Voltaire"
		expected = "Voltaire"
		self.assertEqual(rearrange_name(test_case), expected)

unittest.main()
