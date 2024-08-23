# 영수증

import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prices = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    prices.append(a*b)

if X == sum(prices):
    print("Yes")
else:
    print("No")