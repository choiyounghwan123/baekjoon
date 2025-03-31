# 1922. 네트워크 연결

N = int(input())
M = int(input())

edges = []
parent = [i for i in range(0,N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append([a-1,b-1,c])

edges.sort(key= lambda x: x[2])

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

total_cost = 0

for i in range(M):
    a,b,cost = edges[i]
    if find(a) != find(b):
        union(a,b)
        total_cost += cost
print(total_cost)
