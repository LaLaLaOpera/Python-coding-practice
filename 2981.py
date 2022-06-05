import heapq
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
    heapq.heappush(newList,abs(numList[-i]-numList[-(i+1)]))


answer =0

while True:
    if len(newList) == 1:
        answer = newList[0]
        break
    a = maxdenom(heapq.heappop(newList),heapq.heappop(newList))
    newList.append(a)

answerList = []
for i in range (1, int(answer**(1/2))+1):
    if answer%i == 0:
        answerList.append(i)
        if ((i**2)!=answer):
            answerList.append(answer//i)
answerList.sort()
for i in answerList:
    if i != 1:
        print(i, end=" ")   
