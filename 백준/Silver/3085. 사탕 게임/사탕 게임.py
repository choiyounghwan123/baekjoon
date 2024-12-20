# 3085. 사탕 게임

N = int(input())
board = [list(input()) for _ in range(N)]

def check():
    max_ = 0
    for i in range(N):
        count = 1
        for j in range(1,N):
            if board[i][j-1] != board[i][j]:
                max_ = max(max_,count)
                count = 1
            else:
                count += 1
        max_ = max(max_,count)

    for i in range(N):
        count = 1
        for j in range(1,N):
            if board[j-1][i] != board[j][i]:
                max_ = max(max_, count)
                count = 1
            else:
                count += 1
        max_ = max(max_,count)
    return max_


result = 0

for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            board[i][j],board[i][j+1] = board[i][j+1],board[i][j]
            result = max(result,check())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            result = max(result,check())
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(result)


