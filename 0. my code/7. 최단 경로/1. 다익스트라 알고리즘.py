1. 다익스트라 최단경로 알고리즘
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산
- 음의 간선이 없을때(현실도로는 음의 간선이 없음.)
- 다익스트라 최단경로 알고리즘은 그리디 알고리즘으로 분류(매 상황에서 가장 비용이 적은 노드를 선택)

2. 알고리즘 동작 과정
- 출발노드 설정
- 최단 거리 테이블 초기화
- 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 선택
- 해당노드를 거쳐 다른 노드로 가는 비용계산하여 최단 거리 테이블 갱신
- 위의 두 단계를 반복

## 우선순위 큐을 활용한 다익스트라 알고리즘(백준 1753 최단경로)
import heapq
import sys
input  = sys.stdin.readline
INF = int(1e9)

v,e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(k):
    q = []
    heapq.heappush(q, (0, k))
    distance[k] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(k)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
        
