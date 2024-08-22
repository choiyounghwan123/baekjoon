# 구간 합 구하기 4

import sys

N,M = map(int,sys.stdin.readline().split())
nums = [0] + list(map(int,sys.stdin.readline().split()))

for i in range(1,N+1):
    nums[i] = nums[i-1] + nums[i]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())

    print(nums[j] - nums[i-1])
