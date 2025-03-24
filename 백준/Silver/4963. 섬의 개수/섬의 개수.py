# 4963. 섬의 개수
import sys
sys.setrecursionlimit(10**6)
def dfs(i,j,visited,board):
    visited[i][j] = 1
    dx = [0,0,-1,1,-1,1,-1,1]
    dy = [1,-1,0,0,1,1,-1,-1]
    for k in range(8):
        if 0 <= dx[k] + i < len(board) and 0 <= j + dy[k] < len(board[i]) and not visited[dx[k] + i][dy[k] + j] and board[dx[k] + i][dy[k] + j] == 1:
            dfs(dx[k] + i, dy[k] + j, visited, board)

while True:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == 1:
                dfs(i,j,visited,board)
                count += 1
    print(count)
