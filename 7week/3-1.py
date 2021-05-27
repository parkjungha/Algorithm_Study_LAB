
# u, v로 나누기 
def divide(p): # "()     ))((   ()"	
    count = [0, 0]
    for i in p:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            break
    return p[:sum(count)], p[sum(count):]

# 올바른 문자열인지 체크
def check(p):
    stack = []
    try:
        for i in p:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
        return True
    except:
        return False

# 괄호 방향 뒤집어주기
def convert(u):
    temp = ''
    for i in u:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp

def solution(p):
    answer = '' 

    while len(p) != 0: # 빈 문자열이 아닐 때
        u, p = divide(p)
        if check(u): # 문자열 u가 "올바른 괄호 문자열" 이라면
            answer += u
        else: # 문자열 u가 "올바른 괄호 문자열"이 아니라면 
            answer += '(' + solution(p) + ')' + convert(u[1:-1])
            break

    return answer