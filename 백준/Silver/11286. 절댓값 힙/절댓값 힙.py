# 절대값 힙

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print("0")

    else:
        heapq.heappush(heap,(abs(x),x))
