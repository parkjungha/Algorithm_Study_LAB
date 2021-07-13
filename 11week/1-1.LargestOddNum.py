
# 막 풀었더니 시간초과 뜬 것
def largestOddNumber_(num):
    odd = 0
    for i in range(1,len(num)+1):
        temp = int(num[0:i])
        if temp%2 != 0 and temp > odd:
            odd = temp
    if odd == 0:
        return ("")
    else:
        return(str(odd))

# Back tracking 방법으로 하면 시간 초과 해결
def largestOddNumber(self, num: str) -> str:
    for i in range(len(num)-1, -1, -1):
        if int(num[i])%2 == 1: # 맨 뒤부터 한글자씩 떼서 홀수면
            return num[:i+1] # 처음부터 그 자리까지 바로 리턴 
    return ""