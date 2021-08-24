import heapq
def solution(food_times, k):
    pq = []
    n = len(food_times) # 음식 종류 개수
    for i in range(n): # 우선순위 큐에 (음식 시간, 음식 번호)로 넣어줌
        heapq.heappush(pq, (food_times[i], i+1))
        
    pre_food = 0
    min_food = pq[0][0] # 가장 빨리먹을 수 있는 음식
    
    while True:
        if k-(min_food - pre_food)*n < 0:
            break
        k -= (min_food - pre_food)*n 
    
        heapq.heappop(pq)
        pre_food = min_food
        n -= 1

        if not pq:
            return -1

        min_food = pq[0][0]

        idx = k % n
    # 다시 번호 순으로 정렬 해주고
    pq.sort(key=lambda x: x[1])
    answer = pq[idx][1]
    return answer
    