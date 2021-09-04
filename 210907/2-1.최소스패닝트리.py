
V,E = map(int, input().split())

graph = []

for i in range(E):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])

graph.sort(key=lambda x: x[0]) # 크루스칼 알고리즘은 간선들을 가중치에 따라 정렬이 필요하다

parent = list(range(V + 1)) # [1,2,3, ... ,V] # 처음엔 자기 자신의 값을 담고있는 배열로 초기화. 연결 정보에 따라서 부모 정보를 담아야함

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

sum = 0 # 최소스패닝트리를 구성하는 간선의 비용의 합을 계산
for c, a, b in graph:
    if find(a) != find(b): # a와 b가 연결되어있지 않으면
        union(a, b) # 유니온 ! 
        sum += c

print(sum)