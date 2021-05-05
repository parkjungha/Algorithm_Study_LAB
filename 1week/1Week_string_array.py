# 1 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘.

def isDuplicated1(s):
    if len(set(list(s))) != len(list(s)): 
        return False
    return True

def isDuplicated2(s): # 자료구조를 사용하지 않고 string연산
    for i in range(len(s)):
        if s[i] in s[0:i]+s[i+1:-1]:
            return False
    return True

print(isDuplicated1('abccd')) #False
print(isDuplicated2('abccd')) #False
print(isDuplicated1('abcde')) #True
print(isDuplicated2('abcde')) #True

# 4
def compareStr(s1,s2):
    if abs(len(s1)-len(s2))>1: # 길이 차이가 1 이상 나면 바로 False
        return False

    elif len(s1)==len(s2): # 문자열 길이가 같을 때: 교체
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt>1: 
                return False

    else: # 문자열 길이가 다를 때: 삽입 또는 삭제
        cnt = 0 #  문자열 편집 횟수 count
        j = 0 # s2의 index는 j
        for i in range(len(s1)): # s1의 index는 i
            if s1[i] != s2[j]: # 다를 때
                cnt += 1 # cnt ++
                if cnt>1: # 두번 이상이면 바로 False
                    return False

                if len(s1)>len(s2):
                    i += 1
                elif len(s1)<len(s2):
                    j += 1

            else:
                j += 1
    return True

print(compareStr('pale','ple')) #True
print(compareStr('pale','pales')) #True
print(compareStr('pale','bale')) #True
print(compareStr('pale','bake')) #False

# 5
def stringCompression(s):
    res = ''
    cnt = 1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt += 1
        else:
            res += s[i]+str(cnt)
            cnt = 1
    res += s[i]+str(cnt)
    return res if len(res)<=len(s) else s 
    
print(stringCompression('aabccccaaa')) # a2b1c4a3
print(stringCompression('abcd')) # abcd