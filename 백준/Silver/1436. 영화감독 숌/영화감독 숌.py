# 영화감독 숌

import sys

N = int(sys.stdin.readline())
count = 0
for i in range(666,100000000):
    if "666" in str(i):
        count+=1

        if count == N:
            print(i)
            break