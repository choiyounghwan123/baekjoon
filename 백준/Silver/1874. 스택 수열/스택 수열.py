# 스택 수열

import sys

N = int(sys.stdin.readline())
stack = [1]
nums = [int(sys.stdin.readline()) for _ in range(N)]
k = 2
result = ["+"]
for num in nums:
    while len(stack) == 0 or stack[-1] < num:
        result.append("+")
        stack.append(k)
        k+=1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        result = 0
        break

if result:
    for i in result:
        print(i)