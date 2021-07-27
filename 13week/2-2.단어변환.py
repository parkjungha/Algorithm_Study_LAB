from collections import deque # BFS

'''
 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때,
 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return

'''

def solution(begin, target, words):

    if target not in words:
        return 0 # target이 words에 없으면 바로 리턴 0

    q = deque()
    q.append((begin,0)) # 큐에 시작 단어와 변환 횟수 담기
    
    while q: # 큐가 빌 때까지 반복
        temp,step = q.popleft() # 단어, 변환 횟수 pop 
        for w in words: # 모든 단어에 대해 반복
            
            # 현재 단어와 딱 한글자만 차이나는 단어들만 찾기 => 이걸 인접 노드로 생각하여 BFS 탐색
            diff = 0 
            for i in range(len(w)):
                if temp[i]!=w[i]:
                    diff += 1

            if diff == 1: # 한 글자만 차이나는 단어일때 (인접 노드일때)
                if w == target: # 찾은 단어가 Target이면
                    return step + 1 # 바로 리턴
                q.append((w, step + 1)) # 아니면 Queue에 넣기
    return 0 # 변환할 수 없는 경우

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))