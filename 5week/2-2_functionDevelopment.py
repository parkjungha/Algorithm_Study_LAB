from collections import deque

def solution(progresses, speeds):
    
    answer = deque()
    days = []

    # 남은 시간 계산
    for i in range(len(progresses)):
        remained = 100-progresses[i]
        speed = speeds[i]
        if remained % speed != 0:
            days.append(remained // speed + 1)
        else:
            days.append(remained // speed)

    for i in range(len(days)-1,-1,-1):
        cnt = 1
        while days:
            temp = days.pop()
            if days and days[-1] >= temp:
                cnt += 1
            else:
                answer.appendleft(cnt)
                cnt = 1
            
    return list(answer)

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]))