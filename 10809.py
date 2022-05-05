import sys
from string import ascii_lowercase

result = ""
a = sys.stdin.readline().rstrip()

setList = list(a)

testList = list(ascii_lowercase)
# import를 하기 싫다면 아스키코드를 알파벳으로 변환하여 리스트에 넣어주는 for문을 작성해도 ok
resultList = []

for i in testList:
    if i in setList:
        resultList.append(str(setList.index(i)))
    else:
        resultList.append(str(-1))

result = " ".join(resultList)

print(result)