# 1725. 히스토그램
import sys

input = sys.stdin.readline

N = int(input())
stack = []
result = 0
l = 0

for r in range(N):
    l = r
    x = int(input())

    while stack and stack[-1][0] > x:
        a,l = stack.pop()
        result = max(result, (r-l) * a)
    stack.append([x,l])

while stack:
    a,l = stack.pop()
    result = max(result, (N-l) * a)
print(result)
