# 2563. 색종이

board = [[0 for i in range(100)] for _ in range(100)]

result = 0

for _ in range(int(input())):
    column, row = map(int,input().split())

    for i in range(row,row+10):
        for j in range(column,column+10):
            board[i][j] = 1

for i in board:
    result += sum(i)
print(result)