import heapq
import sys

input = sys.stdin.readline
inf = 10000000000

N, E = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(E):
    a,b,c = map(int, input().split())
    # Point!!!!!!!! 양방향 그래프
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])

stop1, stop2 = map(int, input().split())

def dijkstra(start, end):
    dist = [inf]*N
    dist[start-1] = 0
    q = []
    heapq.heappush(q, [0, start-1])

    while q:
        cost, pos = heapq.heappop(q)

        for p,c in graph[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [c,p])

    return dist[end-1]

# 경로1 -> stop1 -> stop2 -> N
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
# 경로2 -> stop2 -> stop1 -> N
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

if path1 >= inf and path2 >= inf:
    print(-1)
else:
    print(min(path1, path2))