# 11501. 주식

import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    prices = list(map(int,sys.stdin.readline().split()))

    total = 0
    max_price = prices[-1]
    for i in range(N-1,-1,-1):
        if max_price - prices[i] > 0:
            total += max_price - prices[i]
        max_price = max(max_price,prices[i])
    print(total)

