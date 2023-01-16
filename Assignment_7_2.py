# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of
# the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown below. Do not use the sum() function
# or a variable named sum in your solution.
# You can download the sample data at
# http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
counter = 0
output = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter = counter + 1
    print("This is the count: " + " " + str(counter))
    print(line)
    y = slice(21, 28)
    output = output + float(line[y])
    print(float(line[y]))
average = output/counter
print("Average spam confidence: " + str(average))
print("Done")