# 14888. 연산자 끼워넣기

N = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))

min_ = 1e11
max_ = -1e11

def dfs(n,temp):
    if n == N-1:
        global min_, max_
        min_ = min(min_, temp)
        max_ = max(max_,temp)
        return
    if operator[0] != 0:
        operator[0] -= 1
        dfs(n+1,temp + nums[n+1])
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        dfs(n + 1, temp - nums[n+1])
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        dfs(n + 1, temp * nums[n+1])
        operator[2] += 1
    if operator[3] != 0:
        operator[3] -= 1
        dfs(n + 1, int(temp / nums[n+1]))
        operator[3] += 1

dfs(0,nums[0])
print(max_)
print(min_)

