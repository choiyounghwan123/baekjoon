# 13549. 숨바꼭질 3

from collections import deque

N,K = map(int,input().split())

queue = deque([N])
visited = [-1] * 100001
visited[N] = 0
while queue:
    vertex = queue.popleft()

    if vertex == K:
        print(visited[vertex])
        break

    a = vertex*2

    if 0 <= a < 100001 and visited[a] == -1:
        queue.append(a)
        visited[a] = visited[vertex]

    for next in (vertex-1,vertex+1):
        if 0 <= next < 100001 and visited[next] == -1:
            queue.append(next)
            visited[next] = visited[vertex] + 1