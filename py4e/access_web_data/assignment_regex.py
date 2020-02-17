# Assignment: Regular Expressions
# Read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers. 
#       regex_sum_42.txt (There are 90 values with a sum=445833) 
#       regex_sum_373544.txt (There are 78 values and the sum ends with 950)

import re

filename = input("Enter file:")
if len(filename) < 1 : filename = "regex_sum_373544.txt"
handle = open(filename)

number_list = list()
for line in handle:
    line = line.rstrip()
    if len(line) > 0:
        # find all 'numbers' on each line of the file
        numbers = re.findall('[0-9]+', line)
        number_list = number_list + numbers

# convert string list to integers list (using list comprehension)
int_list = [int(i) for i in number_list]

print(sum(int_list))