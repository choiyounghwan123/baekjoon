# 나무 자르기

import sys

N,M = map(int,sys.stdin.readline().split())
lengths = list(map(int,sys.stdin.readline().split()))

start, end = 1,max(lengths)

while start <= end:
    mid = (start+end)//2
    count = 0

    for length in lengths:
        if length-mid > 0:
            count += length-mid

    if M <= count:
        start = mid+1
    else:
        end = mid-1

print(end)



