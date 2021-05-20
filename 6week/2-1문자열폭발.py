
string = input()
bomb = input()

stack = []

for s in string:
    stack.append(s) # 한글자씩 스택에 PUSH 

    if len(stack)>=len(bomb):
        tmp = "".join(stack[-len(bomb):]) 
        if tmp == bomb: # 스택의 위에서부터 폭발 문자열과 같으면 pop
            cnt = 0
            while cnt < len(bomb):
                stack.pop()
                cnt += 1
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))