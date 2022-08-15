문제1: 두 배열의 원소 교체
  동빈이는 두개의 배열A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수.
  동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 
  바꿔치기 연산이란 배열A에 있는 원소 하나와 배열B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다. 
  동빈이의 최종 목표는 배열A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 한다.
  N,K, 그리고 배열A와 B의 정보가 주어졌을때, 
  최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

N,K = map(int, input().split()) # N 원소개수, K 최대 바꿔치기 횟수
A = list(map(int, input().split())) # 배열A
B = list(map(int, input().split())) # 배열B

A.sort()
B.sort(reverse = True)

for i in range(K):
  if A[i] < b[i]:
    A[i], b[i] = b[i], A[i] # 교체
  else: 
    break
print(sum(A))
