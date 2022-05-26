import sys
a,b = (sys.stdin.readline().rstrip()).split()
a,b = list(a), list(b)
a.reverse()
b.reverse()

a = int(a[0]+a[1]+a[2])
b = int(b[0]+b[1]+b[2])

if a>b:
    print(a)
else:
    print(b)
