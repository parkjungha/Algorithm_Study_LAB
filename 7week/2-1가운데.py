# Solution1: 시간초과. heap에 숫자 하나하나 push하고, 중간값에 해당하는 거 pop으로 빼면서 반복

import heapq

n = int(input())
minheap = []

for _ in range(n):
    heapq.heappush(minheap, int(input()))
    tempheap = list(minheap)
    for _ in range((len(tempheap)+1)//2 - 1):
        heapq.heappop(tempheap)
    print(tempheap[0])

# Solution2: 최대힙과 최소힙을 이용하여 중간값을 찾는 방법! 왜 힙을 두개써야하는지 몰라서 구글링함...
import sys
import heapq 

input = sys.stdin.readline # 이거 안하면 시간초과 뜸;;

 # 중앙값 기준으로 작은 값은 최대힙으로, 큰 값은 최소힙으로 구성, 중앙 값은 항상 최대 힙의 첫번째 값을 출력
# (Max Heap) - mid value - (Min Heap)

def insert(minheap,maxheap,x):

    if len(maxheap) == len(minheap): # 크기가 같다면 최대힙에 넣어준다
        heapq.heappush(maxheap,-x)

    else: # 아니면 최소힙에 넣어줌
        heapq.heappush(minheap,x)

    if minheap and -maxheap[0]>minheap[0]: # minheap이 비어있지 않고 최대 힙의 루트는 항상 최소 힙의 루트보다 작게 유지해준다.
        # 최대힙의 루트노드가 더크다면 Swap
        a = heapq.heappop(minheap)
        b = -heapq.heappop(maxheap)
        heapq.heappush(maxheap,-a)
        heapq.heappush(minheap,b)

n=int(input())
minheap, maxheap=[],[]
while n>0:
    n-=1
    insert(minheap,maxheap,int(input()()))
    print(-maxheap[0])