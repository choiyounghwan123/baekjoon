# 괄호

import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    s = list(sys.stdin.readline().rstrip())
    queue = deque()

    check = True

    for i in s:
        if i == "(":
            queue.append(i)
        else:
            if len(queue) == 0:
                check = False
                break
            queue.pop()
    if check and len(queue) == 0:
        print("YES")
    else:
        print("NO")