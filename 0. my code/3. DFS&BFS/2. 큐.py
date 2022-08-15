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
