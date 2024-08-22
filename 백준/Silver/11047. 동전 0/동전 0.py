# 동전 0

import sys

N,K = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
res = 0
while K != 0:
    if K//coins[N-1] >= 1:
        res += K//coins[N-1]
        K = K%coins[N-1]
    N-=1

print(res)
