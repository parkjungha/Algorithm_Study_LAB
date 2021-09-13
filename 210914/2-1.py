import re

def solution(s):
    
    nums = re.findall("\d+", s) # 정규표현식을 사용해서 문자열에서 숫자만 추출하여 리스트로 반환

    freq = {} # 각 숫자 빈도수 카운트해서 Dictionary에 담음
    for i in nums:
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) # 딕셔너리에서 value값으로 내림차순 정렬
    answer = [int(k) for k, v in freq] # 하고 얻은 순서대로의 숫자(key값)가 답

    return answer
    
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))