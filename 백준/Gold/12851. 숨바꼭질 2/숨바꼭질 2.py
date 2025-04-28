# 1697. 숨바꼭질

from collections import deque

N,K = map(int,input().split())
queue = deque([N])
visited = [0] * 100001
result,cnt = 0,0
while queue:
    vertex = queue.popleft()
    if vertex == K:
        result = visited[vertex]
        cnt+=1
        continue

    for i in (vertex - 1, vertex + 1, vertex * 2):
        if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[vertex] + 1):
            queue.append(i)
            visited[i] = visited[vertex] + 1

print(result)
print(cnt)