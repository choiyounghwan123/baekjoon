# 회의실 배정

import sys

N = int(sys.stdin.readline())
times = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda time:(time[1],time[0]))

res = 0
prev_time = 0

for time in times:
    if time[0] >= prev_time:
        res +=1
        prev_time = time[1]

print(res)