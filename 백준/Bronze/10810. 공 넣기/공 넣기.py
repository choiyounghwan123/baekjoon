# 공 넣기

import sys

N,M = map(int,sys.stdin.readline().split())
baskets = [0] * N

for _ in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    for i in range(i-1,j):
        baskets[i] = k

for basket in baskets:
    print(basket, end=" ")
