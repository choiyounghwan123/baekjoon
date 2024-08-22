# 비밀번호 찾기

import sys

N,M = map(int,sys.stdin.readline().split())
hash_map = dict()

for _ in range(N):
    site,password = map(str,sys.stdin.readline().rstrip().split())
    hash_map[site] = password

for _ in range(M):
    print(hash_map[sys.stdin.readline().rstrip()])