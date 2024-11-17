# 10026. 적록색약

import sys

N = int(input())
sys.setrecursionlimit(10**6)

grid = []

for _ in range(N):
    grid.append(list(input().rstrip()))

visited = [[0 for _ in range(N)] for _ in range(N)]

def bfs(i_,j_,color):
    if visited[i_][j_] == 1:
        return

    visited[i_][j_] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        x = i_ + dx[i]
        y = j_ + dy[i]
        if 0<= x < N and 0<= y < N and grid[x][y] == color and visited[x][y] == 0:
            bfs(x,y,grid[x][y])


def bfs1(i_, j_, color):
    if visited[i_][j_] == 1:
        return

    visited[i_][j_] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        x = i_ + dx[i]
        y = j_ + dy[i]
        if color == "R" or color == "G":
            if 0 <= x < N and 0 <= y < N and (grid[x][y] == "R" or grid[x][y] == "G") and visited[x][y] == 0:
                bfs1(x, y, grid[x][y])
        else:
            if 0 <= x < N and 0 <= y < N and grid[x][y] == color and visited[x][y] == 0:
                bfs1(x, y, grid[x][y])

result_one,result_two = 0,0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,grid[i][j])
            result_one += 1

visited = [[0 for _ in range(N)] for _ in range(N)]



for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs1(i,j,grid[i][j])
            result_two += 1


print(result_one)
print(result_two)