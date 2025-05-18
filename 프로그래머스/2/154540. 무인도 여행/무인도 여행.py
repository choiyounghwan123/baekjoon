# 무인도 여행

import sys
sys.setrecursionlimit(100000)

def solution(maps):
    def dfs(i, j):
        print(i,j)
        nonlocal count
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and visited[x][y] == 0 and maps[x][y] != 'X':
                count += int(maps[x][y])
                visited[x][y] = 1
                dfs(x, y)

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = []
    for i in range(len(maps)):
        count = 0
        for j in range(len(maps[i])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                count = 0
                count += int(maps[i][j])
                visited[i][j] = 1
                dfs(i,j)
                answer.append(count)
    return sorted(answer) if answer else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
