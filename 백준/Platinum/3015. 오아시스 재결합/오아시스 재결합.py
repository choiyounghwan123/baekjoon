# 3015. 오아이스 재결합

import sys

input = sys.stdin.readline
N = int(input())
stack = []
result = 0
index = 0
min_ = 2 ** 32
for _ in range(N):
    height = int(input())
    if not stack:
        stack.append([height,1])

    elif stack[-1][0] == height:
        cnt = stack.pop()[1]
        result+= cnt
        if stack:
            result+=1
        stack.append([height,cnt+1])


    elif stack[-1][0] < height:
        while stack and stack[-1][0] < height:
            result+= stack[-1][1]
            stack.pop()
        if stack and stack[-1][0] == height:
            cnt = stack.pop()[1]
            result+=cnt
            if stack:
                result+=1
            stack.append([height,cnt+1])
            continue
        if stack:
            result+=1
        stack.append([height,1])
    else:
        result+=1
        stack.append([height,1])


print(result)