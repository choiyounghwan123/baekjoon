# 공 바꾸기

import sys

N,M = map(int,sys.stdin.readline().split())
baskets = [i for i in range(1,N+1)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    baskets[i-1],baskets[j-1] = baskets[j-1],baskets[i-1]

for basket in baskets:
    print(basket, end=" ")
