# 2841. 외계인의 기타 연주

import sys
input = sys.stdin.readline
N,P = map(int,input().split())
stack = [[0] for _ in range(6)]
result = 0
for i in range(N):
    line, sound = map(int,input().split())
    while stack[line-1][-1] > sound:
        stack[line-1].pop()
        result+=1
    if stack[line-1][-1] == sound:
        continue
    stack[line-1].append(sound)
    result+=1
print(result)
