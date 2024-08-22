# 마인크래프트

import sys

N, M, B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = int(1e9)
glevel = 0

for i in range(257):
    use_block = 0
    take_block = 0

    for y in range(N):
        for x in range(M):
            if board[y][x] > i:
                take_block += board[y][x] - i
            else:
                use_block += i - board[y][x]

    if use_block > take_block + B:
        continue
        
    count = take_block * 2 + use_block    
        
    if count <= ans:
        glevel = i
        ans = count

print(ans, glevel)
