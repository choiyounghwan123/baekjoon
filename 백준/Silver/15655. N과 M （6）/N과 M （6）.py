# 15655. N과 M (6)

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answers = []

def dfs(m,answer,nums):
    if m == 1:
        answers.append(answer)
        return

    for i in range(1,len(nums)):
        dfs(m-1,answer + [nums[i]], nums[i:])

for i in range(N):
    dfs(M,[nums[i]],nums[i:])


for answer in answers:
    for i in answer:
        print(i,end=" ")
    print()