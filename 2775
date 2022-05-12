import sys
a = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]] #리스트속 리스트를 만들고 0층을 만들어준다
for  i in range (1,15): #층수만큼 포문을 반복
    floor = [] #리스트를 생성
    for j in range (0, 14): #호수만큼 포문을 반복
        if j == 0: #1호일 경우 참조할 이전호수가 없으므로 ERROR를 발생시키고
            floor.append(1) #무조건 1이 나오므로 if문을 통해 예외처리해준다
        else:
            floor.append(a[i-1][j]+floor[j-1]) #아랫층의 자신의 값과 해당층에서 전호수를 더한 값과 같으므로 이것을 [i][j]에 append 해준다
    a.append(floor)
    
repeat= int(sys.stdin.readline().rstrip())

for i in range (repeat):
    k= int(sys.stdin.readline().rstrip()) #층수
    n= int(sys.stdin.readline().rstrip()) #호수
    print(a[k][n-1]) #0층부터 시작하지만 문제는 1층부터 구하므로 k는 그대로 n은 1을 빼준다
