# 1-1 이랑 완전 똑같!

N = int(input())
M = int(input())
graph = []

for i in range(M):
    a,b,c = map(int, input().split())
    graph.append([c,a,b])

graph.sort(key = lambda x: x[0])
parent = list(range(N+1))

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if parent[a] == a: # 이미 루트노드
        return a

    parent[a] = find(parent[a])
    return parent[a]

sum = 0
for c,a,b, in graph:
    if find(a) != find(b):
        union(a, b)
        sum += c

print(sum)