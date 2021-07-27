'''
전화번호 목록이 주어질때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램
(한 번호가 다른 번호의 접두어인 경우가 없는 것)
'''

t = int(input())

for _ in range(t):
    # 전화번호 목록 str으로 담고, 사전순 정렬
    numbers = []
    n = int(input())
    for _ in range(n):
        numbers.append(input())
    numbers.sort()
    
    flag = True # 일관성 O
    for i in range(n-1): 
        if numbers[i] == numbers[i+1][0:len(numbers[i])]: # 현재 번호가 다음 번호의 접두어인 경우
            flag = False # 일관성 X
            break # 반복 중단
    
    if flag: 
        print("YES")
    else:
        print("NO")