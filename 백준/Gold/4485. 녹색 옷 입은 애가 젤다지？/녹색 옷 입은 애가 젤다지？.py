# 4485. 녹색 옷 입은 애가 젤다지?
import sys
import heapq
import math
input = sys.stdin.readline
k = 1
while True:
    N = int(input())

    if N == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(N)]
    heap = []
    heapq.heappush(heap,[graph[0][0],0,0])
    costs = [[math.inf] * N for _ in range(N)]
    costs[0][0] = graph[0][0]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while heap:
        coin,r,c = heapq.heappop(heap)

        if costs[r][c] < coin:
            continue

        for i in range(4):
            if 0 <= r + dx[i] < N and 0 <= c +dy[i] < N and costs[r+dx[i]][c + dy[i]] > coin + graph[r+dx[i]][c+dy[i]]:
                costs[r+dx[i]][c + dy[i]] = coin + graph[r+dx[i]][c+dy[i]]
                heapq.heappush(heap,[coin + graph[r+dx[i]][c+dy[i]],r+dx[i],c+dy[i]])
    print(f"Problem {k}: {costs[-1][-1]}")
    k += 1
