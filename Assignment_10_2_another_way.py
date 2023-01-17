# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
fh = open(fname)
counts = dict()
arr = [0] * 24
# print(arr)
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    #print(words)
    hour = words[5]
    #print(hour)
    number = hour.split(":")
    hours = int(number[0])
    #print(hours)
    arr[hours] = arr[hours] + 1
for i in range(0,24):
    if i < 10 and arr[i] > 0:
        print(f"0{i} {arr[i]}")
    elif arr[i] >0:
        print(f"{i} {arr[i]}")