# 공원 산책

from collections import deque


def solution(park, routes):
    start = None
    board = []

    for i in range(len(park)):
        temp = []
        for j in range(len(park[i])):
            if park[i][j] == "S":
                start = [i, j]
                temp.append(1)
            else:
                if park[i][j] == "O":
                    temp.append(1)
                else:
                    temp.append(0)
        board.append(temp)
    directions = dict()
    directions["N"] = [-1, 0]
    directions["S"] = [1, 0]
    directions["W"] = [0, -1]
    directions["E"] = [0, 1]

    for i in range(len(routes)):
        op, n = routes[i].split(" ")
        x = start[0] + directions[op][0] * int(n)
        y = start[1] + directions[op][1] * int(n)
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if directions[op][0] * int(n) != 0:
                if directions[op][0] * int(n) > 0:
                    for i in range(start[0],x+1):
                        if board[i][start[1]] == 0:
                            break
                    else:
                        start = [start[0] + directions[op][0] * int(n), start[1] + directions[op][1] * int(n)]
                else:
                    for i in range(start[0],x-1,-1):
                        if board[i][start[1]] == 0:
                            break
                    else:
                        start = [start[0] + directions[op][0] * int(n), start[1] + directions[op][1] * int(n)]
            elif directions[op][1] * int(n) != 0:
                if directions[op][1] * int(n) > 0:
                    for i in range(start[1], y + 1):
                        if board[start[0]][i] == 0:
                            break
                    else:
                        start = [start[0] + directions[op][0] * int(n), start[1] + directions[op][1] * int(n)]
                else:
                    for i in range(start[1], y-1,-1):
                        if board[start[0]][i] == 0:
                            break
                    else:
                        start = [start[0] + directions[op][0] * int(n), start[1] + directions[op][1] * int(n)]

    return start


print(solution( ["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]))
