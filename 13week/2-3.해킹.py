import heapq,sys

'''
해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 
총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램
'''

input = sys.stdin.readline
inf = 10000000000

def dijkstra(x): # x는 시작 노드
    dist = [inf for i in range(n + 1)] # 무한대로 거리 초기화
    dist[x] = 0 # 시작점은 거리 0
    q = [] # 우선순위 큐
    heapq.heappush(q, [0,x]) # heapq에 삽입할 때 비용이 우선순위가 되어야하기 때문에 비용,노드 순으로 삽입

    while q: # heapq가 빌 때까지 반복
        cost, pos = heapq.heappop(q) # 현재 큐에서 최단거리가 가장 짧은 노드를 꺼내서

        for p,c in graph[pos]: # 현재 노드와 연결된 다른 노드들 모두 확인
            c += cost
            if c < dist[p]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[p] = c # 최단거리 갱신
                heapq.heappush(q, [c,p])

    return dist # 시작노드 x부터 각 노드까지의 최단거리를 담은 List 반환 

testcase = int(input())

for _ in range(testcase):
    n,d,c = map(int,input().split()) # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    graph = [[] for i in range(n+1)]

    for __ in range(d): # 의존성 정보 그래프에 담기
        a,b,s = map(int,input().split())
        graph[b].append([a,s]) # 단방향 그래프 !!

    dist = dijkstra(c)
    maxVal = 0
    cnt = 0
    for d in dist:
        if d != inf: # 감염된 컴퓨터들 (거리가 무한대가 아닌 것)
            cnt += 1
            if maxVal < d: # 가장 거리가 먼 것 (감염되기까지 가장 오래 걸리는 것)
                maxVal = d # 업데이트

    print(cnt, maxVal) # 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간