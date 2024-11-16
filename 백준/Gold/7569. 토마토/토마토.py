# 7569. 토마토

import collections
import sys

M, N, H = map(int, input().split())
box = []
queue = collections.deque()

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append((i, j, k))
    box.append(temp)

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        x_ = x + dx[i]
        y_ = y + dy[i]
        z_ = z + dz[i]
        if 0 <= x_ < M and 0<=y_<N and 0<=z_<H and box[z_][y_][x_] == 0:
            queue.append((z_,y_,x_))
            box[z_][y_][x_] = box[z][y][x] + 1

day = 0

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            day = max(day,max(j))
print(day-1)




