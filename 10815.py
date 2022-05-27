import sys
a = int(sys.stdin.readline().rstrip())
b = list(map(int,sys.stdin.readline().rstrip().split()))

dic = {}
for i in range (len(b)):
    dic[b[i]] = 1 #가지고있는 숫자는 dic에 1이라는값으로 저장
c = int(sys.stdin.readline().rstrip())
d = list(map(int,sys.stdin.readline().rstrip().split()))


for i in range(c):
    try: print(dic[d[i]], end=" ")#값이 있으면 dic의 값을 불러오고
    except: 
        ValueError
        print(0, end=" ") #없으면 에러가 생기니 0을 프린트하는것으로 처리
