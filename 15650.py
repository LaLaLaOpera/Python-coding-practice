import sys
sys.setrecursionlimit(10**7)
a,b = map(int,sys.stdin.readline().rstrip().split())
lst = [0] #처음부터 비교가 필요해 0이라는 기본값을 넣어준다
def numChar():
    if len(lst) == b+1: #0이 추가되었으므로 배열은 1개더 긴 값을 잡아주고
        newList = [] #기존값을 건드리면 재귀함수를 건드리게되므로 새로운 배열을 생성/초기화
        for i in lst: #기존배열에서 임으로 추가한
            if i !=0: #0을 빼주는것으로
                newList.append(i) #새로운 배열을 만든다
        print(" ".join(map(str, newList)))
        return
    else:
        for i in range(1,a+1):
            if i > lst[-1]:
                if i not in lst:
                    lst.append(i)
                    numChar()
                    lst.pop()
numChar()
