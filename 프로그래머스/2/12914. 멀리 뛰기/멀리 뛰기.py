# [프로그래머스] 멀리 뛰기

def solution(n):
    answer = 0
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

print(solution(1))