# 1043. 거짓말
import sys
input = sys.stdin.readline


N,M = map(int,input().split())
knows = set(input().split()[1:])
parties = []

for _ in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for party in parties:
        if knows & party:
            knows = knows.union(party)

cnt = 0
for party in parties:
    if party & knows:
        continue
    cnt += 1
print(cnt)