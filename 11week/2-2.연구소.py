from collections import deque
from copy import deepcopy

n,m = map(int,input().split())
array = []
virus = []
for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)

dx= [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0 # 안전 영역의 최대 크기

def bfs():
    global ans
    temp = deepcopy(array) # 원본 어레이 저장해두기
    safe = 0

    q = deque()
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:  # deque에 모든 바이러스 다 넣음
                q.append((i,j)) # virus 좌표 다 queue에 담음

    while q: # queue가 빌 때까지 반복
        x,y = q.popleft()
        for i in range(4): # 현재 바이러스 위치에서 상하좌우로 이동하면서
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny] == 0: # 이동할 칸이 범위 안에 속하고, 인접한 칸이 빈칸이면(벽이 아니면), 바이러스 퍼뜨림
                temp[nx][ny] = 2 # 바이러스 감염시킴
                q.append((nx,ny)) # 바이러스 감염된 칸 queue에 넣음
    
    # 안전영역의 크기 구하기. N*M 매트릭스 한칸한칸 돌면서 0인 것 개수 세기
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    ans = max(ans,safe) # 최대값만 저장

# 벽 세울 수 있는 모든 경우의 수에 대해서 벽 세우는 함수
def wall(cnt):

    if cnt==3: # 벽 세개 다 세웠으면
        bfs() # 바이러스 퍼뜨려보고 안전 영역 개수 세기. 이 과정에서 계속 ans이 안전영역의 최댓값으로 업데이트됨
        return

    else: # 벽 3개 아직 덜세웠으면
        for i in range(n):
            for j in range(m):
                if array[i][j]==0: # 빈칸이면
                    array[i][j] =1 # 벽 설치하고   
                    wall(cnt+1) # count 1 증가시키고, 바뀐 어레이로 recursion으로 들어감
                    array[i][j] = 0 # 어레이 복원해줌

wall(0)

print(ans)