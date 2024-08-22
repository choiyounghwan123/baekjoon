# 요세푸스 문제 0

import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

queue = deque([i for i in range(1,N+1)])
res = []
while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print("<",end="")

for i in range(N):
    if i == N-1:
        print(res[i],end="")
    else:
        print(res[i],end=", ")

print(">")
