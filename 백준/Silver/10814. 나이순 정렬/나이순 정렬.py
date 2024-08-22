# 나이순 정렬

import sys

info = [list(map(str,sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline()))]

for i in sorted(info,key=lambda j:int(j[0])):
    print(i[0],i[1])
