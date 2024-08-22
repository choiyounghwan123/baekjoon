# 나머지 합

import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
prefix_sum = [0] * (N+1)
result = 0
r = [0] * M

for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
    remainder = prefix_sum[i] % M
    if remainder == 0:
        result += 1
    r[remainder] += 1

for i in range(M):
    if r[i] > 1:
        result += (r[i] * (r[i]-1)) // 2
print(result)


