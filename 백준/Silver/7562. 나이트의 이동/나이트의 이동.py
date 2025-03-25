# 7562. 나이트의 이동

from collections import deque

N = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(N):
    I = int(input())

    board = [list(0 for _ in range(I)) for _ in range(I)]

    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    board[startX][startY] = 1
    queue = deque([(startX, startY)])

    while queue:
        x, y = queue.popleft()

        if x == endX and y == endY:
            print(board[x][y]-1)
            break
        for i in range(8):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if 0 <= x_ < I and 0 <= y_ < I and (board[x_][y_] == 0 or board[x_][y_] > (board[x][y] + 1)):
                board[x_][y_] = board[x][y] + 1
                queue.append([x_, y_])


