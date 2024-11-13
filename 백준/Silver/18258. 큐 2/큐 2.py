# 18258. 큐 2

import sys
input = sys.stdin.readline
T = int(input())

import collections
queue = collections.deque()

for _ in range(T):
    command = list(map(str,input().split()))

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    else:
        if queue:
            print(queue[-1])
        else:
            print("-1")