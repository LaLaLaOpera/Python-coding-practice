import sys
a,b = map(int,sys.stdin.readline().rstrip().split())
check = {}
for i in range (a):
    check[sys.stdin.readline().rstrip()] = 1

for i in range (b):
    try:
        check[sys.stdin.readlin().rstrip()] += 1
    except: KeyError

result = [key for key, value in check.items() if value >= 2]

print(len(result))
for i in result:
    print(i)
