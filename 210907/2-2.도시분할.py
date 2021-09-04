'''
2-2 도시 분할 계획

정점의 개수 N, 간선의 개수 M, 양방향 그래프가 주어질 때,
두 개의 Sub-Graph로 분할.  각 Sub-Graph는 최소 스패닝 트리의 조건을 만족해야함.

풀이 : 2-1 문제와 동일하게 최소 스패닝 트리를 먼저 구한다. 
    여기서는 두 마을로 분리해야하니까 가장 마지막에 추가된 간선 (비용이 가장 높은) 간선을 제거한다.

Python3로 하면 시간초과, PyPy3로 하면 통과.
'''

N,M = map(int, input().split())

graph = []

for i in range(M):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])

graph.sort(key=lambda x: x[0]) # 크루스칼 알고리즘은 간선들을 가중치에 따라 정렬이 필요하다

parent = list(range(N + 1)) # [1,2,3, ... ,V] # 처음엔 자기 자신의 값을 담고있는 배열로 초기화. 연결 정보에 따라서 부모 정보를 담아야함


# 유니온-파인드는 그래프 알고리즘으로 두 노드가 같은 그래프에 속하는지 판별하는 알고리즘
# 노드를 합치는 Union연산과 노드의 루트 노드를 찾는 Find연산으로 이루어짐

def union(a,b): 
    a = find(a) ## 각각 find 연산을 통해 루트 노드를 찾음
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]: # 자기자신의 값을 담고 있다면 본인이 루트 노드인것.
        return a
    parent[a] = find(parent[a]) # recursion으로 부모 계속 찾음
    return parent[a] # 루트 노드 반환

mst = [] # 최소스패닝트리를 구성하는 간선의 비용을 담을 리스트. 
for c, a, b in graph:
    if find(a) != find(b): # a와 b가 연결되어있지 않으면
        union(a, b) # 유니온 ! 
        mst.append(c)

mst.pop() # 마지막에 추가된 간선 제거 
print(sum(mst))