# 16928. 뱀과 사다리 게임

from collections import deque

N,M = map(int,input().split())
board = [0] * 101
visited = [False] * 101

ladder = dict()

for _ in range(N):
    x,y = map(int,input().split())
    ladder[x] = y

snake = dict()

for _ in range(M):
    u,v = map(int,input().split())
    snake[u] = v

queue = deque([1])
visited[1] = True
visited[0] = False

while queue:
    node = queue.popleft()
    if node == 100:
        print(board[100])
        break
    for i in range(1,7):
        x = node + i
        if x <= 100 and not visited[x]:
            if x in ladder:
                x = ladder[x]
            if x in snake:
                x = snake[x]
            if not visited[x]:
                visited[x] = True
                queue.append(x)
                board[x] = board[node] + 1