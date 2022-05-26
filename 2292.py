import sys
a= int(sys.stdin.readline().rstrip())
n = 1
limit = 8

while True:
    if a == 1: #입력값이 1인경우의 수를 따로 둔다
        print(1)
        break
    else:
        if a < limit: 
            print(n+1)
            break
        else:
            n += 1
            limit += n*6 #조건을 만족하지 못할때마다 매번 증가값을 6씩 늘려간다
