# Assignment 2.3
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.


# This first line is provided for you
hrs = input("Enter Hours: ")
# exception check: ensure hours is a 'numeric'
try:
    hours = float(hrs)
except:
    hours = -1

rt = input("Enter Rate: ")
# exception check: ensure rate is a 'numeric'
try: 
    rate = float(rt)
except:
    rate = -1

if hours != -1 and rate != -1:
    print("Pay:", hours*rate)
else:
    print("Invalid input for Hours.")
