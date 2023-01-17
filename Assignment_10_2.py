# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
fh = open(fname)
counts = dict()
# arr = [0] * 24
# print(arr)
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    hr = words[5].split(":")
    counts[hr[0]] = counts.get(hr[0], 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((key, val))

lst.sort()
for key, val in lst:
    print(key, val)
    # #print(words)
    # hour = words[5]
    # #print(hour)
    # number = hour.split(":")
    # hours = int(number[0])
    # arr[hours] = arr[hours] + 1
    # print(hours)

    # for hour in lst:
    #     hours = hour.split(":")
    #     print(hours)
    # print(type(words))
    # print(words[0])
