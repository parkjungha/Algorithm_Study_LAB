'''
2-2 단지 번호 문제와 유사한듯
미찬가지로 DFS/BFS관계 없이 하나의 노드에서 시작해서 그래프 탐색을 통해 방문 표시함
방문할 수 있는 모든 노드들을 방문하고 재귀를 마치고 나오면 하나의 네트워크를 만든 것 (앞선 문제의 단지 하나랑 동일함)

전체 노드 돌면서 아직 방문표시 되어있지 않은 노드들에 대해서 DFS 탐색하기
'''

def solution(n, computers): # n은 node의 개수, computers는 Adjacency Matrix 
    answer = 0
    visit = [0 for _ in range(n)]
    for i in range(n):
        if visit[i] == 0: # 아직 방문하지 않은 노드들만
            dfs(i,n,visit,computers) # 탐색
            answer += 1 # 탐색이 끝나면 하나의 네트워크를 구성하는 가능한한 모든 노드를 찾은 것임
    return answer

# DFS는 Recursion을 이용해서 구현.
def dfs(start,n,visit,computers):
    visit[start] = 1 # 해당 노드 방문 표시
    for i in range(n):
        if computers[start][i] == 1 and visit[i] == 0: # 해당 노드와 연결되어 있고, 아직 방문하지 않은 노드이면 recursion으로 그 노드로 들어감
            dfs(i,n,visit,computers)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))