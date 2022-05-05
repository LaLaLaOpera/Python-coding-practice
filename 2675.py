a = int(input())


for i in range (a):
    b = input().split()
    textList = []
    for i in b[1]:
        textList.append(i)
    result = ""
    for i in range (len(textList)):
        for j in range (int(b[0])):
            result += textList[i]
    print(result)