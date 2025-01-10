# 9465. 스티커

for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    if N == 1:
        print(max(stickers[0][0],stickers[1][0]))
        continue

    stickers[1][1] += stickers[0][0]
    stickers[0][1] += stickers[1][0]

    for k in range(2,N):
        stickers[0][k] += max(stickers[1][k-1],stickers[1][k-2])
        stickers[1][k] += max(stickers[0][k-1],stickers[0][k-2])
    print(max(stickers[1][N-1],stickers[0][N-1]))

