# 랜선 자르기

import sys

K,N = map(int,sys.stdin.readline().split())
res = 0
lines = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1,max(lines)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for line in lines:
        num += line // mid

    if num >= N:
        start = mid+1
    else:
        end = mid - 1

print(end)