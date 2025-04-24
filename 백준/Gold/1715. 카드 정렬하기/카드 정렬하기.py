# 1715. 카드 정렬하기

import sys
import heapq
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    heapq.heappush(nums, int(input()))

res = 0

while len(nums) != 1:
    a,b = heapq.heappop(nums),heapq.heappop(nums)
    heapq.heappush(nums,a+b)
    res += a+b

print(res)
