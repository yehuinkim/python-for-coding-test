재귀함수: 자기자신을 다시 호출하는 함수 
재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다. 단, 더 어려운 형태의 코드가 될 수 있다. 
모든 재귀함수는 반목문을 이용하여 동일한 기능을 구현할 수 있다. 
재귀함수가 반복문보다 유리한 경우, 불리한 경우 둘 다 존재.
컴퓨터가 함수를 연속적으로 호출화면 컴퓨터 메모리 내부의 스택 프레임이 쌓인다. 
따라서 스택을 사용해야할 때 구현상 스택 라이브러리 대신 재귀함수를 이용하는 경우가 많다. 

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

# 최대공약수 계산 (유클리드 호제법)
유클리드 호제법: 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하면, A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
/: 나누기 //: 나눗셈의 몫, % 나눗셈의 나머지, divmod(): 나눗셈의 몫과 나머지(튜플형식)
def gcd(a,b):
  if a%b == 0:
    return b
  else: 
    return gcd(b, a%b)
print(gcd(192,162))

