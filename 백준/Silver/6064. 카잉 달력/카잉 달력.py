# 카잉 달력

import sys

T = int(sys.stdin.readline())


def cal(M: int, N: int, x: int, y: int) -> int:
    k = x

    while k <= M*N:
        if (k-x) % M == 0 and (k-y) % N == 0:
            return k
        k+=M
    return -1

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    print(cal(M,N,x,y))
