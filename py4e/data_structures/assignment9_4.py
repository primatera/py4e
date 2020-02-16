# Assignment 9.4
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

# create histogram of email addresses
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != "From" :
        continue
    if words[0] == "From" :
        emails[words[1]] = emails.get(words[1],0) + 1

# determine 'mode' of email addresses
max_count = None
max_email = None
for email,count in emails.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, max_count)
