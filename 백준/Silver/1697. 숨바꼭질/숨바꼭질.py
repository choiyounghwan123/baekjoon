# 숨바꼭질

import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
vistied = [0] * (100001)

queue = deque([N])

while queue:
    vertex = queue.popleft()

    if vertex == K:
        print(vistied[vertex])
        break

    for next_vertex in (vertex-1,vertex+1,vertex*2):
        if 0<= next_vertex < 100001 and not vistied[next_vertex]:
            vistied[next_vertex] = vistied[vertex] + 1
            queue.append(next_vertex)