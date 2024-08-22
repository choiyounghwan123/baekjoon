import sys

for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    dp = [[i for i in range(1,N+1)]]

    for i in range(1,K+1):
        for j in range(N):
            if j == 0:
                dp.append([1])
            else:
                dp[i].append(dp[i][j-1] + dp[i-1][j])
    print(dp[K][N-1])