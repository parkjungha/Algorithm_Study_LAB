
# 인접행렬 형식으로 출력. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력
# n개의 모든 정점을 시작노드로 잡고 DFS 탐색한 후에 visit 리스트를 확인하여 방문되었다면 1, 아니면 0으로 출력. 이걸 n 번 반복

n = int(input()) # node

adj = [] # Adjacency Matrix 형식으로 입력받음
for i in range(n):
    adj.append(list(map(int, input().split())))

visit = [0 for i in range(n)] # 특정 시작노드 v를 기준으로 방문 되었는지 안되었는지 표시하기 위함.



def dfs(v): # 시작노드 v에 대해서 DFS 탐색
    for i in range(n):
        if visit[i] == 0 and adj[v][i] == 1: # 방문하지 않았고, edge가 존재한다면
            visit[i] = 1
            dfs(i)



for i in range(n):
    dfs(i) # 이걸 끝나면 visit 리스트가 업데이트될 것
    
    for j in range(n):
        if visit[j] == 1: # 방문되었으면, 즉 정점 i에서 j로 가는 경로가 있으면 1
            print(1,end=' ')
        else: # 없으면 0
            print(0, end=' ')
    print() # 노드 하나 끝나면 줄바꿈을 위해
    visit = [0 for i in range(n)] # visit 초기화시켜줌