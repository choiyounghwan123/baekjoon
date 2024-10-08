# 최대 힙

import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap,-x)