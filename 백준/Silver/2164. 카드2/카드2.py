# 카드2

import sys
from collections import deque

queue = deque([i for i in range(1,int(sys.stdin.readline())+1)])

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])