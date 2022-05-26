import sys
a =int(sys.stdin.readline()) #반복할 횟수를 받아준다
c = [0]*8001 #counting을 위해 0으로 이루어진 리스트를 주어진 범위만큼 생성해주고
d = [] #이전 문제와 달리 메모리 제한이 없으니 전체를 받아줄 리스트도 생성한다
for i in range (a):
    b = (int(sys.stdin.readline())) 
    d.append(b) 
    c[b+4000] += 1 #값의 범위가 -4000~4000이므로 받아온 값에 4000을 더한값에 해당하는 인덱스의 카운트를 하나올린다
count = 0 #중앙값을 찾기위한 카운트를 생성한다
commVal = 0 #중앙값을 저장할 변수를 생성
for i in range (len(c)):
    count += c[i] #for문을 돌면서 c[i]에 해당하는값(해당 인덱스의 값을 가진 수들의 카운트) 를 카운트에 더해주고
    if count >= a/2: #만약 이것이 수 전체의 갯수의 절반과 동일하거나 그것을 초과한 시점에서
        commVal = i #그 인덱스 값을 저장하고
        break #포문을 종료시킨다
mostc = c.index(max(c)) #가장큰 값이 가장 많이 등장한 최빈값이므로 그 인덱스 값을 저장한다

try: #문제 조건이 최빈값이 2개 이상이라면 두번째로 작은 값을 출력하라고했으니
    nextc = c.index(max(c),mostc+1) #최빈값 다음부터 다시 최빈값을 구하고
    if c[mostc] == c[nextc]: #만약 그것이 처음구한값과 같다면
        mostc = nextc #그 다음값을 최빈값에 대입시킨다
except: ValueError #값이 없거나 에러가 생길 수 있으므로 except 구문을 통해 예외처리를 만들어준뒤
mind = min(d) #저장해둔 d리스트에서 최소값과 최대값을 각각 구해준뒤
maxd = max(d)

print(round(sum(d)/a)) #평균
print(commVal-4000) #중간값
print(mostc-4000) #최빈값
print(maxd-mind) #범위를 출력한다
