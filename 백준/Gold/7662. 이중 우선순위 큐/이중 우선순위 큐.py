# 7662. 이중 우선순위 큐

import heapq
import sys
import collections

for _ in range(int(sys.stdin.readline())):
    max_heap =[]
    min_heap = []
    hash_map = collections.defaultdict(int)
    for _ in range(int(sys.stdin.readline())):
        command, n = map(str,sys.stdin.readline().rstrip().split())
        if (max_heap or min_heap) and command == "D":
            if n == "-1" and min_heap:
                hash_map[heapq.heappop(min_heap)] -= 1

            elif n == "1" and max_heap:
                hash_map[-heapq.heappop(max_heap)] -= 1
            while min_heap and hash_map[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            while max_heap and hash_map[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
        elif command == "I":
            hash_map[int(n)] += 1
            heapq.heappush(max_heap, -(int(n)))
            heapq.heappush(min_heap, int(n))
    if max_heap and min_heap:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
    else:
        print("EMPTY")