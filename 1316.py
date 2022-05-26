import sys
a = int(sys.stdin.readline().rstrip())
count = 0
for i in range (a): #a의 길이만큼 입력을 반복하는 for문
    checkList = [] #checkList는 매번 초기화 시켜준다
    b = (sys.stdin.readline().rstrip())
    for j in b:
        checkList.append(j) #j라는 값을 입력해주고 그때마다
        if checkList.index(j) != (len(checkList)-1): #j 값을 인덱스해서 그게 마지막값인지 아닌지 확인한다
            if checkList[-1] != checkList[-2]: #만약 아니라면 이전의 값과 같은지 다른지 확인하고
                count += 1 #아니라면 카운트를 하나 올리고 j in b 포문을 종료시킨다
                break
print(a-count)
