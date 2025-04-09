# 1202. 보석 도둑

import heapq
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dia = []
for _ in range(N):
    weight, cost = map(int,input().split())
    heapq.heappush(dia, [weight,cost])

weights = [int(input()) for _ in range(K)]
weights.sort()

result = 0
tem_data = []
for weight in weights:
    while dia and dia[0][0] <= weight:
        heapq.heappush(tem_data, -heapq.heappop(dia)[1])
    if tem_data:
        result += -heapq.heappop(tem_data)
    if not dia and not tem_data:
        break
print(result)
