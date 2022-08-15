재귀함수: 자기자신을 다시 호출하는 함수 

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


