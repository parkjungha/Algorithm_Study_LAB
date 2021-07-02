from collections import deque # For BFS

# BFS는 Queue 자료구조를 이용해서 구현.
def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1 # 첫 노드 방문 표시

    while queue: # queue가 빌 때까지 반복
        v = queue.popleft() 
        print(v, end=' ')

        for i in range(len(graph[start])): # start node와 연결된 노드 모두 돌면서
            if graph[v][i] == 1 and visit[i] == 0: # 해당 노드와 연결되어 있으면서, 아직 방문하지 않은 노드일 때 탐색 시작
                queue.append(i) # queue에 추가하고
                visit[i] = 1 # 방문 표시

# DFS는 Recursion을 이용해서 구현.
def dfs(start):
    print(start,end=' ')
    visit[start] = 1 # 해당 노드 방문 표시
    for i in range(1,n+1):
        if graph[start][i] == 1 and visit[i] == 0: # 해당 노드와 연결되어 있고, 아직 방문하지 않은 노드이면 recursion으로 그 노드로 들어감
            dfs(i)



n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)] # N*N 크기의 Adjacency Matrix 생성
visit = [0 for _ in range(n+1)] # 방문한 노드인지 아닌지 저장하기 위해서

# Edge 연결 관계에 따라서 Adjacency Matrix 만들기
for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
visit = [0 for _ in range(n+1)] # visit 배열 초기화
print() # 한줄 띄워
bfs(v)