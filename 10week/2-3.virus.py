'''
2-1과 거의 그대로 구현
Adjacency Matrix 만든 후에
1번 노드(1번 컴퓨터)를 시작 노드로 해서
dfs든 bfs든 상관없이 그래프 탐색 시킴
방문된 (visit=1이 된) 노드는 감염된 것. 
'''

n = int(input()) # node
e = int(input()) # edge

graph = [[0]*(n+1) for _ in range(n+1)] # N*N 크기의 Adjacency Matrix 생성
visit = [0 for _ in range(n+1)] # 방문한 노드인지 아닌지 저장하기 위해서

# Edge 연결 관계에 따라서 Adjacency Matrix 만들기
for _ in range(e):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# DFS는 Recursion을 이용해서 구현.
def dfs(start):
    visit[start] = 1 # 해당 노드 방문 표시
    for i in range(1,n+1):
        if graph[start][i] == 1 and visit[i] == 0: # 해당 노드와 연결되어 있고, 아직 방문하지 않은 노드이면 recursion으로 그 노드로 들어감
            dfs(i)

dfs(1)

cnt = 0
for i in visit:
    if i == 1:
        cnt += 1            
            
print(cnt-1) # dfs탐색 후 방문된 노드의 개수에서 1번 컴퓨터는 제외해야하니까 -1          