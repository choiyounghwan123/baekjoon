# 패션왕 신해빈

import sys
from itertools import combinations

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    hash_map = dict()
    for _ in range(N):
        name, type = map(str, sys.stdin.readline().split())
        hash_map[type] = hash_map.get(type, 0) + 1

    res = 1

    for i in hash_map:
        res *= hash_map[i] + 1

    print(res - 1)
