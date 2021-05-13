def solution(N, stages):
    answer = {}
    for s in range(1,N+1):
        nom = stages.count(s) # 분자
        denom = len([x for x in stages if x >= s]) # 분모
        answer[s] = nom / denom
    answer = sorted(answer.items(), key=lambda x:x[1], reverse=True) # Dictionary의 Value값으로 정렬해서 결과를 Key만 List로 반환
    return [a[0] for a in answer]


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))