import sys
a= int(sys.stdin.readline().rstrip())

for i in range (a):
    h,w,n= map(int,sys.stdin.readline().rstrip().split())
    k = 1
    j = 1
    k += ((n-1)%h)
    j += ((n-1)//h)
    print(k*100+j)
