# 14500. 테트로미노

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * M for _ in range(N)]

maximum = 0


def dfs(n, m, cnt, depth):
    global maximum

    if depth == 4:
        maximum = max(maximum, cnt)
        return

    for i in range(4):
        nx, ny = m + dx[i], n + dy[i]
        if nx >= M or ny >= N or nx < 0 or ny < 0 or visited[ny][nx]:
            continue

        if depth == 2:
            visited[ny][nx] = True
            dfs(n,m,cnt + board[ny][nx],depth+1)
            visited[ny][nx] = False

        visited[ny][nx] = True
        dfs(ny,nx,cnt + board[ny][nx],depth + 1)
        visited[ny][nx] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

print(maximum)
