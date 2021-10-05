# 시간초과 코드

def solution(stones, k):
    cnt = 0
    answer = 0

    while True: # 한명씩 한명씩 건너게 하기
        for i in range(len(stones)):
            if stones[i] == 0:
                cnt += 1
            else:
                stones[i] -= 1
                cnt = 0

            if cnt == k: # 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k 를 넘어서면 끝.
                return answer
        answer += 1
    
    return answer

# 이진 탐색을 통해 최대 몇 명까지 징검다리를 건널 수 있는지
# mid 값과 stone 의 값을 비교해서 mid 값보다 작은 구간이 연속적으로 k개 이상이면 mid = right - 1로 업데이트
#                                                                   미만이면 mid = left + 1로 업데이트.

def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 1
    while left <= right:
        mid = (left+right) // 2
        blank = 0
        flag = True
        for stone in stones:
            if stone < mid:
                blank += 1
                if blank == k: # 건널 수 없음 -> 반복문 중단하고 최대값 하나 내림
                    flag = False
                    break 
            else:
                blank = 0
        
        if flag:
            answer = max(answer, mid)
            left = mid + 1 # 최소값을 올려봄
        else:
            right = mid - 1 # 최대값을 내림

    return answer