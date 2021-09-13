def solution(k, room_number):
    
    occupy = [] # 배정된 방

    for room in room_number:
        if room not in occupy: # 아직 배정되지 않은 방이면
            occupy.append(room) # 배정시킴
        else: # 이미 배정된 방이면
            for i in range(room+1,k+1): # 원하는 방보다 번호가 크면서 가장 번호가 작은 방 순서대로
                if i not in occupy: # 비어있으면
                    occupy.append(i) # 배정시킴
                    break 
            
    return occupy