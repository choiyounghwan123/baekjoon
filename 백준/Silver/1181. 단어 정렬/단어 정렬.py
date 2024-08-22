# 단어 정렬

import sys

N = int(sys.stdin.readline())

s = list(set(sys.stdin.readline().rstrip() for _ in range(N)))

for j in sorted(s,key=lambda i: (len(i),i)):
    print(j)