# 16953. A -> B
from collections import deque

A,B = map(int,input().split())
queue = deque([[A,1]])
while queue:
    node,cnt = queue.popleft()
    if node == B:
        print(cnt)
        exit()

    if node < B:
        queue.append([node * 2,cnt + 1])
        queue.append([int(str(node) + "1"),cnt + 1])
    else:
        continue
print(-1)

