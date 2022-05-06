import sys

a = sys.stdin.readline().rstrip()

a = a.upper()
count = 0
textList = []
countList = []
for i in range(65, 91):
    textList.append(chr(i))
for i in range (26):
    countList.append(0)

for i in a:
    if i in textList:
        countList[textList.index(i)] += 1

for i in countList:
    if i == max(countList):
        count += 1
if count == 1:
    print(textList[countList.index(max(countList))])
else:
    print('?')
