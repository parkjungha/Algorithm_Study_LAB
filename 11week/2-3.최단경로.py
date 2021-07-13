'''
다익스트라 알고리즘은 한 노드에서 모든 다른 노드까지의 최단거리를 구하는 알고리즘

'''

import math
import heapq
import sys

input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V)] 

for _ in range(E):
    x,y,w = map(int,input().split())
    graph[x-1].append([y-1,w])

def dijkstra(v,k,g):
    dist = [math.inf]*v
    dist[k-1] = 0 # 시작점은 0 
    q = [] # 우선순위 큐
    heapq.heappush(q, [0,k-1]) # heapq에 삽입할 때 비용이 우선순위가 되어야하기 때문에 비용,노드 순으로 삽입

    while q: # heapq가 빌 때까지 반복
        cost, pos = heapq.heappop(q)
        
        for p,c in g[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [c,p])
    return dist

for d in dijkstra(V, K, graph):
    print(d if d != math.inf else "INF")