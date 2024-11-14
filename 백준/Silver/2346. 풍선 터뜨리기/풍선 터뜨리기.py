# 2346. 풍선 터뜨리기

import sys
from collections import deque

N = int(input())
balloon = list(map(int,sys.stdin.readline().split()))

queue =deque()

for i in range(N):
    queue.append((balloon[i],i+1))

result = []

while queue:
    num,index = queue.popleft()
    result.append(index)
    if num > 0 and queue:
        for _ in range(num-1):
            queue.append((queue.popleft()))

    elif num < 0 and queue:
        for _ in range(abs(num)):
            queue.appendleft(queue.pop())

# -5 -5 -5 -5 -5
print(*result)



