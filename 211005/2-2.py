# *는 10, 0은 11, #는 12로 간주

def solution(numbers, hand):
    answer = ''
    lastL = 10 # 왼손의 현재 위치: *
    lastR = 12 # 오른손의 현재 위치: #
    
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            lastL = n
        elif n in [3,6,9]:
            answer += 'R'
            lastR = n
        
        # [2,5,8,0] 일때, 상 하 좌 우 -3 +3 -1 1 이동
        # 마지막 손의 위치와 2,5,8,0 원소간 절댓값을 구하고 이를 3으로 나눈 몫과 나머지를 더하면 키패드 상의 거리임.
        else: 
            n = 11 if n == 0 else n # 0이면 11로 간주
            
            absL = abs(n - lastL)
            absR = abs(n - lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)): # 왼손이 더 멀때
                answer+='R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)): # 오른손이 더 멀때
                answer +='L'
                lastL = n
            else: # 같을 때
                if hand == 'left': # 왼손잡이이면
                    answer+='L'
                    lastL = n
                else: # 오른손잡이이면
                    answer+='R'
                    lastR = n
                
    return answer