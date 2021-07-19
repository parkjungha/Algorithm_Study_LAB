

def eliminateMaximum(dist, speed):
    time = []
    for i in range(len(dist)):
        time.append(dist[i]/speed[i]) # 시간 = 거리 / 속력
    time.sort() # 제일 빨리 오는 순으로 정렬

    for i in range(len(dist)): # i는 시간(초)의 흐름
        if time[i] <= i: # 몬스터가 i초가 지나기 전에 이미 왔으면 진거
            return i 

    return len(dist) # 초가 끝나면 다 물리친거


