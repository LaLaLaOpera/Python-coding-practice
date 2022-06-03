def maxdenom(x,y):
    if x< y:
        x, y = y, x
    if y == 0:
        return x
    if x%y == 0:
        return y
    else:
        return maxdenom(y, x%y)

import sys
n = int(sys.stdin.readline().rstrip())
numList = []
newList = []
for i in range (n):
    numList.append(int(sys.stdin.readline().rstrip()))

for i in range(n):
    newList.append(abs(numList[-i]-numList[-(i+1)]))

for i in range(n):
    maxdenom(newList[-i],newList[-(i+1)])
