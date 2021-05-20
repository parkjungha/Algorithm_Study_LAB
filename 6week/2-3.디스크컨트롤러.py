
# 평균을 가장 줄이려면 SJF (shortes job first) 알고리즘으로 처리해야함. 따라서 소요시간 기준으로 jobs 정렬 => heapq를 쓰거나, 그냥 list sort를 하거나

### SOLUTION1 : 그냥 list 정렬

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    jobs = sorted(jobs,key = lambda x:x[1]) # 소요시간 기준으로 jobs 정렬
    
    while jobs: # jobs가 빌 때까지
        for i in range(len(jobs)):
            if jobs[i][0] <= time: # 현재 시간보다 jobs의 요청 시간이 작으면, 
                time += jobs[i][1] # 해당하는 job처리. 
                answer += time - jobs[i][0] # 해당 job의 요청에서 종료까지 시간
                jobs.pop(i) # 처리한 job pop. (시간 복잡도 O(n^2)?..)
                break
            if i == len(jobs)-1 : # 반복문 다 돌았는데, 현재 시간에 처리할 수 있는 일이 없을 때
                time += 1
                
    return answer//n # 소수점은 버림 

### SOLUTION2 : Heapq사용

import heapq
def solution(jobs):
    answer = 0
    time = 0 # 현재 시점
    start = -1 # 바로 이전에 완료한 작업의 시작 시간. 초기화는 -1로
    heap = []

    i = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time: # 현재 시점에서 처리할 수 있는 작업들을 모두 힙에 넣을건데
                heapq.heappush(heap,[j[1],j[0]]) # 소요시간 기준으로 최소힙 만들어짐 (그래서 순서바꿔서)

        if heap:
            curr = heapq.heappop(heap) # 최소 소요시간인거 pop
            start = time 
            time += curr[0] # 소요시간만큼 time에 더해줌
            answer += time - curr[1] # 해당 job의 요청에서 종료까지 시간
            i += 1

        else: # 힙이 비어있으면 (= 현재 시점에서 처리할 수 있는 작업이 하나도 없다면) time ++
            time += 1
    
    return answer//len(jobs)