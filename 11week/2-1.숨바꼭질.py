from collections import deque
n,k = map(int,input().split())
visit = [0]*100001

def bfs():
    queue = deque()
    queue.append(n) # 시작점
    while queue: # queue가 빌 때 까지 반복
        x = queue.popleft()
        if x == k: # 목적지에 도착하면 멈추고 시간 출력
            print(visit[x]) 
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and visit[nx]==0: # 이동할 칸이 범위를 벗어나지 않고, 아직 방문하지 않았다면
                visit[nx] = visit[x]+1 # 방문하는데 현재 칸 시간에서 +1 한 값
                queue.append(nx)
bfs()