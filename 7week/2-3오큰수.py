n = int(input())
a = list(map(int,input().split()))

res = [-1]*n
stack = []

for i in range(n):
    while stack and stack[-1][0] < a[i]: # stack이 비어있지 않고, stack의 top의 값이 현재 값보다 작을 때
        val, idx = stack.pop() # 작은 값을 pop 
        res[idx] = a[i] # pop된 값의 오큰수는 현재 값으로 할당
    stack.append([a[i],i])

for r in res:
    print(r,end=' ')

