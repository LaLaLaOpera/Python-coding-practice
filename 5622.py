import sys
a = (sys.stdin.readline().rstrip())
a.lower()
a = list(a)

count = 0
for i in a:
    if ord(i) <= 67:
        count += 3
    elif ord(i) <= 70:
        count += 4
    elif ord(i) <= 73:
        count += 5
    elif ord(i) <= 76:
        count += 6
    elif ord(i) <= 79:
        count += 7
    elif ord(i) <= 83:
        count += 8
    elif ord(i) <= 86:
        count += 9
    else:
        count += 10

print(count)
