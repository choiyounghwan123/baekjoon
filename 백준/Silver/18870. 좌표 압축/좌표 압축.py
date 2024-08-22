# 좌표 압축

import sys

N = int(sys.stdin.readline())
coordinate = list(map(int,sys.stdin.readline().split()))
a = sorted(list(set(coordinate)))

hash_map = dict()
for i in range(len(a)):
    hash_map[a[i]] = i
for i in range(N):
    print(hash_map[coordinate[i]],end=" ")

