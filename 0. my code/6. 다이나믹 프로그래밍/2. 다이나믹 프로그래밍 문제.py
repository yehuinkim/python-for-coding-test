문제1. 1로 만들기 (백준1463)
x = int(input())

d = [0]*1000001
for i in range(2, x+1):
    d[i]=d[i-1]+1
    if i%3 == 0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2 == 0:
        d[i]=min(d[i],d[i//2]+1)
print(d[x])

문제2. 개미전사
N = int(input())
k = list(map(int, input().split()))

d = [0]*101
d[0] = k[0]
d[1] = max(k[0],k[1])

for i in range(2,N):
  d[i] = max(d[i-1], d[i-2]+k[i])

print(d[n-1])

문제3. 바닥공사(백준11727)
n = int(input())
d=[0]*1001
d[1]=1
d[2] = 3

for i in range(3,n+1):
    d[i]=(d[i-1]+2*d[i-2])%10007
print(d[n])

문제4. 효율적인 화폐구성
n,m = map(int, input().split())
array=[]
for i in range(n):
  array.append(int(input()))

d=[10001]*(m+1)
d[0]=0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] !=1001:
      d[j]=min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])

