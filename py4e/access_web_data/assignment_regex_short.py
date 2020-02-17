# Assignment: Regular Expression (short hand version) using list comprehension

import re

filename = input("Enter file:")
if len(filename) < 1 : filename = "regex_sum_373544.txt"
handle = open(filename)

# List Comprehension - short version
print( sum( [ int(i) for i in re.findall('[0-9]+',handle.read()) ] ) )
