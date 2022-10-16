다이나믹 프로그래밍은 문제가 다음의 조건을 만족할때 사용할 수 있음. 
1. 최적부분구조:큰 문제를 작은문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결해야 함.

대표적인 예: 피보나치 수열
def fibo(x):
  if x ==1  or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)
print(fibo(4))

## 메모이제이션(탑다운방식,하향식)-재귀식
d = [0]*100
def fibo(x):
  if x ==1  or x==2:
    return 1
  if d[x]!=0:
    return d[x]
  d[x] = fibo(x-1)+fibo(x-2)
  return d[x]
print(fibo(99))

d = [0]*100
def fibo(x):
  print('f('+str(x)+')', end = ' ')
  if x == 1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1)+fibo(x-2)
  return d[x]
fibo(6)

## 바텀업 방식
d = [0]*100
d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]

print(d[n])


