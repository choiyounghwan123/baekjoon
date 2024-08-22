# 듣보잡

import sys

N,M = map(int,sys.stdin.readline().split())

hash_map = dict()

for i in range(N):
    x = sys.stdin.readline().rstrip()
    hash_map[x] = i+1
result = []
for _ in range(M):
    x = sys.stdin.readline().rstrip()
    if x in hash_map:
        result.append(x)

print(len(result))

for i in sorted(result):
    print(i)