from collections import deque
n = int(input())
array = []

for i in range(n):
    array.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    array[x][y] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4): # array에서 상,하,좌,우 돌면서
            nx = x+dx[i] # x좌표 이동할 칸
            ny = y+dy[i] # y좌표 이동할 칸
            if 0<=nx<n and 0<=ny<n: # array 범위를 벗어나지 않을 때
                if array[nx][ny] == 1: # 이웃이면
                    array[nx][ny] = 0 # 0으로 표시. 방문했음.
                    q.append((nx,ny)) # queue에 추가
                    cnt += 1 # 각 단지에 속하는 집의 수 count하는 거
    count.append(cnt) # queue가 비었다는건 더이상 연결된 집이 없다는 것. 즉 하나의 단지 끝.

for i in range(n):
    for j in range(n):
        if array[i][j] == 1: # array내의 모든 단지에 대해서 bfs 탐색하여 집 개수 count해야 함
            bfs(i,j)

count.sort()
print(len(count))
for i in count:
    print(i)