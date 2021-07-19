'''
플로이드-워셜 알고리즘(Floyd-Warshall Algorithm)은 그래프에서 모든 꼭짓점 사이의 최단 경로의 거리를 구하는 알고리즘
시간 복잡도는 O(n^3) 삼중 for문

'''

import sys

inf = 100000000
input = sys.stdin.readline

n = int(input())
m = int(input())

d = [[inf]*n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if d[a-1][b-1] > c:
        d[a-1][b-1] = c

for k in range(n): # k는 거쳐가는 노드
    for i in range(n): # i는 시작 노드
        for j in range(n): # j는 도착 노드
            # 자기 자신으로 오는 경우
            if i==j:
                d[i][j] = 0
                
            # i에서 j로 바로 가는 비용과, i에서 k를 거치고 j로 가는 경우를 비교
            else:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                    
for i in range(n):
    for j in range(n):
        if d[i][j] == inf:
            print(0, end = ' ')
        else:
            print(d[i][j], end = ' ')
    print()