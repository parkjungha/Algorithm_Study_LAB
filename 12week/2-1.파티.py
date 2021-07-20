# 지난주 2-3 최단경로 문제랑 매우 유사하게 해결
# 다익스트라 알고리즘은 한 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘
# 이 문제는 왕복이기 때문에 (각 노드에서 X까지 가는 거리 + X에서 각 노드까지 가는 거리)의 합을 계산, 가장 큰 것을 리턴

import heapq

N,M,X = map(int,input().split())
inf = 10000000000
graph = [[] for _ in range(N)]

# 노드의 개수가 n이고 시작노드가 x이고 graph가 주어질 때, 노드 x로부터 다른 n-1개의 노드까지의 최단거리가 담긴 dist 리스트를 반환하는 함수
def dijkstra(n,x,graph):
    dist = [inf]*n # 무한대로 거리 초기화
    dist[x] = 0 # 시작점은 거리 0
    q = [] # 우선순위 큐
    heapq.heappush(q, [0,x]) # heapq에 삽입할 때 비용이 우선순위가 되어야하기 때문에 비용,노드 순으로 삽입

    while q: # heapq가 빌 때까지 반복
        cost, pos = heapq.heappop(q) # 현재 최단거리가 가장 짧은 노드를 꺼내서

        for p,c in graph[pos]: # 현재 노드와 연결된 다른 노드를 확인
            c += cost
            if c < dist[p]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[p] = c # 최단거리 갱신
                heapq.heappush(q, [c,p])

    return dist


for i in range(M):
    a,b,t = map(int,input().split())
    graph[a-1].append([b-1, t])

ans = [0]*N

for i in range(N):
    temp = dijkstra(N, i, graph) # 각각의 노드를 시작노드로 하여 최단거리 계산

    if i == X-1: # 파티 장소일때, 파티장소에서 각각의 노드까지 돌아가는 거리를 ans 리스트에 더해주어야함
        for idx, r in enumerate(temp):
            ans[idx] += r
    else:
        ans[i] += temp[X-1] # 각 시작 노드에서부터 파티장소 X까지 가는 거리를 ans 리스트에 더해줌

print(max(ans))