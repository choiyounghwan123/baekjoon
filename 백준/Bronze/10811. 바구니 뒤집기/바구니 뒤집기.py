# 바구니 뒤집기

import sys

N,M = map(int,sys.stdin.readline().split())
baskets = [i for i in range(1,N+1)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]
for basket in baskets:
    print(basket,end=" ")