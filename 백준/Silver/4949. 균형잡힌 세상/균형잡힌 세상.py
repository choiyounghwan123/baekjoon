# 균형잡힌 세상

import sys
from collections import deque

while True:
    s = list(sys.stdin.readline().rstrip())

    if s[0] == "." and len(s) == 1:
        break

    queue = deque()
    check = 1
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            queue.append(s[i])
        elif s[i] == "]":
            if len(queue) == 0 or queue[-1] != "[":
                check = 0
                break
            queue.pop()
        elif s[i] == ")":
            if len(queue) == 0 or queue[-1] != "(":
                check = 0
                break
            queue.pop()

    if check and len(queue) == 0:
        print("yes")
    else:
        print("no")
