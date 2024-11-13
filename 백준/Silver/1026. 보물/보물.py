# 1026. 보물

import heapq

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

heap = []
A.sort()
for i in range(N):
    heapq.heappush(heap, -B[i])

result = 0

for i in range(N):
    b = heapq.heappop(heap)
    result += -(b * A[i])

print(result)
