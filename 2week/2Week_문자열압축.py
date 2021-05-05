import sys
def solution(s):
    minLen = sys.maxsize
    res = ''
    
    if len(s)==1:
        return 1
    
    for i in range(1,len(s)//2+1): # i는 문자열 자를 단위 개수
        temp = s[0:i] # 첫 i개의 문자로 초기화
        cnt = 1 
        for j in range(i,len(s),i): # i만큼 ++
            if s[j:j+i] == temp: # 같으면
                cnt += 1 # cnt 증가
            else: # 다를 때
                if cnt == 1: # cnt가 1이면 안써줌
                    res += temp
                else: # 1이 아니면 cnt랑 문자열
                    res += str(cnt)+temp
                temp = s[j:j+i] # temp는 다음 i만큼으로 업데이트
                cnt = 1 # cnt도 1으로 업데이트
                
        if cnt == 1: # 맨 마지막에 남은 문자열에 대해서
            res += temp 
        else:
            res += str(cnt)+temp
        minLen = min(minLen,len(res)) # 더 작은 값 반환
        res = '' # i가 바뀔때마다 새로 계산해줘야해서 초기화
    
    return minLen 


# 저번주 문제 참고함
# def stringCompression(s):
#     res = ''
#     cnt = 1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             cnt += 1
#         else:
#             res += s[i]+str(cnt)
#             cnt = 1
#     res += s[i]+str(cnt)
#     return res if len(res)<=len(s) else s 