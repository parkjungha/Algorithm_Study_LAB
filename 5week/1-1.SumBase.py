
def sumBase(n, k):
    res = ''
    if k == 10: # 10진수면 변환 필요 X
        res = str(n)
    else:
        while n!=0: # n을 k로 나눈 몫이 0이될 때까지 반복
            res += str(n%k) # 나머지를 string으로 바꿔서 저장
            n = n//k
    ans = 0
    for s in res:
        ans += int(s)
    return ans