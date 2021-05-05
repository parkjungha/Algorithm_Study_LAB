def solution(record):
    answer = []
    
    users = {} # 유저아이디 (key) : 닉네임 (value) 를 담을 Dictionary 
    
    for i in range(len(record)):
        record[i] = record[i].split() # 각 string element를 [명령어, 유저 아이디, 닉네임] 리스트 object로 바꿈
        
        if record[i][0] == 'Enter' or record[i][0] == 'Change':
            users[record[i][1]] = record[i][2] # users dictionary Update함.
        
    for i in range(len(record)): # Result 출력
        if record[i][0] == 'Enter':
            answer.append(users[record[i][1]]+"님이 들어왔습니다.")
        if record[i][0] == 'Leave':
            answer.append(users[record[i][1]]+"님이 나갔습니다.")
    
    return answer