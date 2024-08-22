# 큐

import sys
from collections import deque

queue = deque()

for _ in range(int(sys.stdin.readline())):
    order = list(map(str,sys.stdin.readline().rstrip().split()))

    if len(order) == 1:
        if order[0] == "front":
            if len(queue):
                print(queue[0])
            else:
                print("-1")
        elif order[0] == "size":
            print(len(queue))
        elif order[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif order[0] == "back":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
    else:
        queue.append(order[1])

