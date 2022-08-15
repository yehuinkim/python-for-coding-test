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
