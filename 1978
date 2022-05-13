import sys
a = int(sys.stdin.readline().rstrip()) #다른 언어를 위해 있던 값
b = list(map(int,sys.stdin.readline().rstrip().split())) #한줄에 있는 값을 리스트로 가져옴
checkList = []
for i in range (1, max(b)+1): #리스트에 있던 최대값까지 구함
    if i == 1: #지금보니 리스트를 2부터 시작하게하고 이부분을  생략해도 됐음
        continue
    elif i == 2: #checkList에 최초값은 필요하니 2는 소수리스트에 더해줌
        checkList.append(i) 
    else:
        count = 0 #카운트를 0으로두고
        for j in checkList: #체크리스트에있는 수만큼 만복
            if i%j != 0: #소수일경우 1과 자기 자신만으로 나눠지므로
                count += 1 #소수리스트에 있는 모든 값과 나눴을때 안나눠졌을때만 카운트를 추가하고 
                if count == len(checkList): #그 수가 체크리스트 전체길이와 가까워졌다면 소수이므로
                    checkList.append(i) #그 값을 체크리스트에 추가
            else:
                break #만약 아니라면 거기서 포문을 종료시킨다
result = list(set(b) & set(checkList)) # b리스트와 체크리스트의 교집합을 구하고
print(len(result)) #교집합의 길이 = 입력값이 가진 소수의 
