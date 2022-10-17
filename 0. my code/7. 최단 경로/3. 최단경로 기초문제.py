문제1. 미래도시

import sys
input = sys.stdin.readline
n, m = map(int,input().split())
INF = 101
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0
# 간선 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split())

# 플로이드 알고리즘 점화식 적용
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][k]+graph[k][x]
if distance >= INF:
  print('-1')
else:
  print(distance)
-----------------------------------------------------------------------------
문제2. 전보

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())
graph =[[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x,y,z = map(int, input().split())
  graph[x].append((y,z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  distance[start]=0
  while q:
    dis, now = heapq.heappop(q)
    if distance[now]< dis:
      continue
    for i in graph[now]:
      cost = dis +i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(cost, i[0])

dijkstra(start)
count = 0
max_distance = 0
for i in distance:
  if i != INF:
    count += 1
    max_distance = max(i, max_distance)

print(count-1, max_distance)
