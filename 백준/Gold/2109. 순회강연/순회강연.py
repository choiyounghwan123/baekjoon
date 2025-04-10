# 2109. 순회강연

import heapq

N = int(input())
pays = []

for _ in range(N):
    pays.append(list(map(int,input().split())))
pays.sort(key= lambda x: x[1])
temp = []

for i in range(N):
    heapq.heappush(temp, pays[i][0])
    if len(temp) > pays[i][1]:
        heapq.heappop(temp)
print(sum(temp))



