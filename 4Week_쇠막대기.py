'''
1. '(' 이면 push
2. '()' 이면 pop, 레이저에 의해서 쇠막대기 있는거 다 한번씩 잘림. 즉 조각 개수 stack에 들어있는 '('의 개수만큼 더해줌
3. ')' 이면 pop, 그냥 쇠막대기 하나가 끝났다는 뜻이니까 1만큼만 더해줌
'''

s = list(input())
stack = []
ans = 0

for i in range(len(s)):
    if s[i] == '(': #1
        stack.append(s[i])
    elif s[i] == ')': #2
        if s[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else: #3
            stack.pop()
            ans += 1

print(ans)