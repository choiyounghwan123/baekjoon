# 14501. 퇴사

N = int(input())

works = [list(map(int,input().split()))for i in range(N)]
works.insert(0,0)
dp = [0] * (N + 2)

for i in range(1,N+1):
    for j in range(i+works[i][0], N+2):
        dp[j] = max(dp[i]+ works[i][1],dp[j])

print(dp[-1])


