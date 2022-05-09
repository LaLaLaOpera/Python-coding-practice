a = input()
a = list(a)
check = ['c=', 'c-','d-', 'lj', 'nj', 's=', 'z='] #체크해야할 2자리를 가진 문자들
count = 0

for j in check:
    for i in range(len(a)-1): //2글자씩 체크하므로 전체길이에서 1을 빼주어 인덱스에서 벗어나는것을 방지한다.
        if a[i]+a[i+1] == j:
            count += 1 
for i in range(len(a)-2):
    if a[i]+a[i+1]+a[i+2] =='dz=': //마지막 3글자짜리 예외 'z=' 가 'dz=' 이였을 경우의 수가 있으므로 한번 더 빼준다.
        count += 1
print(len(a)-count) //모든 예외를 다 카운트했으므로 전체 길이에서 카운트를 빼준값이 크로아티아 알파벳의 총 길이가 된다.
