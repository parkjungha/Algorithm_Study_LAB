import sys

inf = 1000000000
n,m = map(int,input().split())
d = [[inf]*n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1 # x,y간의 대소관계가 존재하면 1, 모르면 0

for k in range(n): # 거쳐가는 노드
    for i in range(n): # 시작 노드
        for j in range(n): # 도착 노드
            if d[i][k] + d[k][j] == 2: # k를 거쳐서 i와 j가 도달할 수 있다면
                d[i][j] = 1 # 대소관계가 존재하는 것!

# 인접 행렬을 돌면서 대소관계가 있는 노드들에 대해 cnt++
# i와 j의 대소관계가 존재하면, cnt의 i번째와 j번째 값을 증가시킨다
# 이 값이 전체 노드수에서 자기자신을 뺀 n-1과 같다면 자신의 키가 몇번째인지 알 수 있는 것
cnt = [0]*n
for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            cnt[i] += 1 
            cnt[j] += 1
print(cnt.count(n-1))