# 5430. AC

import collections
import sys

for _ in range(int(input())):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = collections.deque(x)
    if n == 0:
        queue = []
    r = 0
    for command in p:
        if command == "R":
            r += 1
        else:
            if len(queue) < 1:
                r = -1
                print("error")
                break
            else:
                if r % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if r != -1:
        if r % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
