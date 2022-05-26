import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
checkList = []
for i in range (1, b+1):
    if i == 1:
        continue
    elif i == 2:
        checkList.append(i)
    else:
        count = 0
        for j in checkList:
            if i%j != 0:
                count += 1
                if count == len(checkList):
                    checkList.append(i)
            else:
                break

numList = []
for i in range (a, b+1):
    numList.append(i)

result = (set(numList) & set(checkList)) 

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
