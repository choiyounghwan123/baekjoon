# N과 M (12)

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))


def dfs(result,cnt,nums_):
    if cnt == M:
        print(*result)
        return
    prev = -1
    for i in range(len(nums_)):
        if nums_[i] != prev:
            dfs(result + [nums_[i]],cnt + 1, nums_[i:])
        prev = nums_[i]


dfs([],0,nums)