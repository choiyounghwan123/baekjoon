# [프로그래머스] 네트워크

from collections import deque

def dfs(i,computer,visited):
    for j in range(len(computer)):
        if computer[i][j] == 1 and not visited[j]:
            visited[j] = 1
            print(j)
            dfs(j,computer,visited)
def solution(n, computers):
    visited = [0] * n
    result = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                visited[i] = 1
                print(i,j)
                dfs(i,computers,visited)
                result += 1

    return result



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))