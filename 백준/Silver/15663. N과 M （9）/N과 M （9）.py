# 15663. N 과 M(9)

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

result = []

def dfs(cnt,sequence,visited):
    if cnt == M:
        result.append(sequence)
        return
    prev = -1
    for i in range(N):
        if i in visited or prev == nums[i]:
            continue
        prev = nums[i]
        dfs(cnt + 1, sequence + [nums[i]],visited + [i])

dfs(0,[],[])

for i in result:
    print(*i)




