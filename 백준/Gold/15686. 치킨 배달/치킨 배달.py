# 15686. 치킨 배달
import sys
input = sys.stdin.readline
home = []
chicken = []
N,M = map(int,input().split())

for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j] == 1:
            home.append([i+1,j+1])
        elif row[j] == 2:
            chicken.append([i+1,j+1])
visited = [False] * len(chicken)
min_ans = 1000000
def dfs(idx,m):
    global min_ans
    if m == M:
        ans = 0
        for i in range(len(home)):
            distance = 1000000
            for j in range(len(chicken)):
                if visited[j]:
                    distance = min(distance, abs(home[i][0] - chicken[j][0]) + abs(home[i][1] - chicken[j][1]))
            ans += distance
        min_ans = min(min_ans,ans)
        return

    for i in range(idx,len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,m+1)
            visited[i] = False
dfs(0,0)
print(min_ans)