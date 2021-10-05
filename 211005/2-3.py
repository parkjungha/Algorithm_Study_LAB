from itertools import permutations
import re

def solution(expression):
    oper = []
    if '*' in expression:
        oper.append('*')
    if '+' in expression:
        oper.append('+')
    if '-' in expression:
        oper.append('-')
    
    oper = list(permutations(oper)) # 가능한 모든 우선순위의 조합 구하기: 순열
    expression = re.split('([^0-9])', expression) # 숫자를 제외한 문자로 split 

# "100-200*300-500+20"

# ['100', '-', '200', '*', '300', '-', '500', '+', '20']

    max_sum = 0
    for ops in oper: # 가능한 모든 우선순위 조합에 대해서 다 해봄
        expression_copy = expression[:]
        for op in ops: # 우선순위 순서대로 연산자 하나씩 먼저 연산하기
            while op in expression_copy:
                op_idx = expression_copy.index(op) # 연산자의 index값
                cal = str(eval(expression_copy[op_idx-1] + expression_copy[op_idx] +expression_copy[op_idx+1]))
                expression_copy[op_idx-1] = cal
                expression_copy = expression_copy[:op_idx] + expression_copy[op_idx+2:]
        
    max_sum = max(max_sum, abs((int(expression_copy[-1])))) # 최대값 갱신
    return max_sum