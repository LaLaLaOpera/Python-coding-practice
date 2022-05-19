import sys
a,b = map(int,sys.stdin.readline().split())
c = list(sys.stdin.readline().split())
c = list(map(int,c))
min = b

for i in c:
    for j in c:
        if i !=j:
            for k in c:
                if k!=j and k!=i:
                    if i+j+k<=b and b-(i+j+k)<min:
                        min = b-(i+j+k)


print(b-min) #브루트 포스라서 단순 반복이 많다. 더 줄일 수 있을지는 생각해봐야할듯?
