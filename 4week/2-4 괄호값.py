
string = input()
stack = []

def check(string): # 올바른 괄호열인지 체크
    stackCheck = [] # 체크를 위한 Stack
    pair = {'(':')','[':']'}
    for s in string:
        if s in "([": # 여는 괄호이면 push
            stackCheck.append(s)
        elif s in ")]": # 닫는 괄호이면 
            if not stackCheck or pair[stackCheck[-1]] != s: # Stack이 비어있거나, 짝이 안맞을 때
                return False 
            stackCheck.pop() # 짝이 맞으면 pop
    return len(stackCheck) == 0 # string 다 돌았는데 아직 stack에 뭔가 남아있으면 False 반환

def calculate(string):
    for s in string:
        if s in "([": #1 여는 괄호이면 push
            stack.append(s)

        elif s == ')': #2 ')' 일때
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0

                for i in range(len(stack)-1,-1,-1): # stack의 뒤에서부터 짝을 찾음
                    if stack[i] == '(':
                        stack[-1] = temp*2
                        break
                    else:
                        temp += stack[i]
                        stack.pop()

        elif s == ']': #3 ']' 일때
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0

                for i in range(len(stack)-1,-1,-1): # stack의 뒤에서부터 짝을 찾음
                    if stack[i] == '[':
                        stack[-1] = temp*3
                        break
                    else:
                        temp += stack[i]
                        stack.pop()
    return sum(stack)

if check(string): # 올바른 괄호일때만 계산
    print(calculate(string))
else:
    print(0)