import heapq
import sys

input = sys.stdin.readline # 시간초과 떠서 추가함

n = int(input())
heap = []
    
for i in range(n):
    m = int(input())
    if m == 0:
        if len(heap) == 0:
            print(0) # 힙이 비어있으면 0 출력
        else:
            print(heapq.heappop(heap)) # 최솟값 출력
    else:
        heapq.heappush(heap,m) # Push