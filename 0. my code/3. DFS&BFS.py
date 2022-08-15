1. 스택 
스택 자료구조는 먼저 들어온 데이터가 나중에 나가는 형식으로 선입후출의 자료구조이다. 
입구와 출구가 동일한 형태로 시각화. 박스 쌓기 예시 

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack[::-1])
print(stack)

2. 큐
먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다.
입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화.

from collections import deque

queue = deque() # 큐 구현을 위해 deque 라이브러리 사용
queue.append(5) #삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #왼쪽에 위치한 것 삭제 5 삭제
queue.append(1)
queue.append(4)
queue.popleft() # 2 삭제

print(queue) # 먼저 들어온 순서대로 출력하기 
queue.reverse() # 역순으로 바꾸기 
print(queue) #나중에 들어온 원소부터 출력

<b>3. 재귀함수
자기자신을 다시 호출화는 함수 

# 무한히 반복되는 재귀함수: 무한루프를 이용할 것이 아니라면 종료조건을 보통 넣어준다. 
def recursive_function():
  print('재귀함수를 호출합니다.')
  recursive_function()
  
# 종료조건이 있는 재귀함수 
def recursive_function(i):
  if i==100 :
    return # 100번째 호출을 했을 때 종료하도록 조건 명시 
  print(i, '번째 재귀함수에서', i+1, '번째 재귀함수까지를 호출합니다.')
  recursive_function(i+1)
  print(i,'번째 재귀함수에서 종료합니다.')
recursive_function(1)

# 팩토리얼-반복적으로 구현: 1부터 n까지의 수 차례대로 곱하기
def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

print('반복적으로 구현:', factorial_iterative(5))
# 팩토리얼-재귀적으로 구현: n이 1 이하인 경우 1을 반환, n! = n * (n-1)!
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

print('재귀적으로 구현:', factorial_recursive(5))
