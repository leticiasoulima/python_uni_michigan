# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
file = open(fname)
count = dict()

for line in file:
    if line.startswith('From ') :
        words = line.split()
        time = words[5]
        hs = time[:2]
        count[hs] = count.get(hs,0) + 1

for k, v in sorted(count.items()):
    print (k, v)
