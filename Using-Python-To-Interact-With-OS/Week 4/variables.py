#!/usr/bin/env python3

import os

# os.environ.get(<if the key exists>, <if the key doesn't exist>)
print(f"HOME: {os.environ.get('HOME','')}")
print(f"HOME: {os.environ.get('SHELL','')}")
print(f"FRUIT: {os.environ.get('FRUIT','')}")