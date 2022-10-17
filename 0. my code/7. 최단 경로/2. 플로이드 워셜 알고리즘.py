1. 플로리드 워셜 알고리즘
- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 매 단계마다 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
- 2차원 테이블에 최단 거리 정보를 저장
- 다이나믹 프로그래밍 유형에 속한다. 
- 노드 개수가 적은 상황에서 주로 사용하고 노드의 개수가 많은 경우는 다익스트라 알고리즘을 주로 사용
- 점화식 Dab = min(Dab, Dak+Dkb)

### 플로이드 (백준 11404)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

#행렬 만들기
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신으로 가는거 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0
# 간선 정보
for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
    
# 플로이드 알고리즘 점화식 적용
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF: 
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
