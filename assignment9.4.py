fname = input("Enter file:")
hand = open(fname)
lst = list()
for line in hand:
    if line.startswith("From:"):
        line = line.split()
        lst.append(line[1])
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1
bigCount = None
bigWord = None
for key,value in counts.items(): 
    if bigCount is None or value > bigCount:
        bigCount = value
        bigWord = word
print (bigWord,bigCount)
