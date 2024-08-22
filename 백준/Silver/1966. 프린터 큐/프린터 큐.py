# 프린터 큐

import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N,M = map(int,sys.stdin.readline().split())
    importance = list(map(int,sys.stdin.readline().split()))
    queue = deque(importance)
    res = 0
    m = M
    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())
        else:
            if m == 0:
                break
            queue.popleft()
            res+=1
        m = len(queue)-1 if m == 0 else m-1

    print(res+1)







