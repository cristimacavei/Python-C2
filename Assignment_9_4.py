# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

fname = input("Enter file:")
fh = open(fname)
max = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    # print(words[1])
    max[words[1]] = max.get(words[1], 0) + 1

largest = None
biggest_sender = None

for key in max:
    if largest is None:
        #print("In largest")
        largest = max[key]
    else:
        if max[key] > largest:
            #print("Here`1")
            largest = max[key]
            biggest_sender = key

print(biggest_sender, largest)

