def solution(gems):
    unique = list(set(gems))
    i = 0  # start 
    j = len(unique)-1 # end
    while j < len(gems):
        isTrue = True
        for u in unique:
            if u not in gems[i:j+1]: # unique에 있는 모든 원소들이 gem[i:j]에 포함되면, (하나라도 없으면 바로 break)
                isTrue = False # 모든 종류의 보석을 하나 이상씩 포함하지 않음 !!!!!!
                break
        if isTrue:
            break
        j += 1
    
    if j <= len(unique):
        return [1,j+1]
    
    while i < j-len(unique)+1:        
        for u in unique:
            if u not in gems[i:j+1]:
                isTrue = False 
                break
        if isTrue: # 다 포함하면
            i += 1

    return [i,j+1]

def solution2(gems):
    unique = len(set(gems)) # 종류개수
    total = len(gems) # 진열대 길이
    answer = []
    start, end = 0, 0  
    dis, idx = 0, 1 # 구간, index
    # 초기값
    cur_shop = {gems[0]: 1}
    while start < total and end < total:
        if len(cur_shop) < unique: # 아직 전체 모음 아님
            end += 1
            if end == total:
                break
            cur_shop[gems[end]] = cur_shop.get(gems[end], 0) + 1
        else:
            answer.append((end-start, [start+1, end+1]))
            cur_shop[gems[start]] -= 1
            if cur_shop[gems[start]] == 0:
                del cur_shop[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[dis], x[idx]))
    return answer[0][idx]