import sys
num = 1
while True:
  num= int(sys.stdin.readline().rstrip())
  if num == 0:
    break
  numList = [] 
  for i in range (num+1,(num*2)+1):
    numList.append(i)
  
  a = [False,False] + [True]*((num*2)-1) #에라토네스의 체를 그대로 이용
  primes=[]
  for i in range(2,num*2+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i, (num*2+1), i):
          a[j] = False

  result = list(set(numList)&(set(primes)))     
  result.sort()
  print(len(result)) #리스트의 길이를 출력
