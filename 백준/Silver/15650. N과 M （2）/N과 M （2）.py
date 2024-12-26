# 15650. N과 M (2)

N,M = map(int,input().split())

answers = []

def dfs(i,m,nums):
    if m == 1:
        answers.append(nums)
        return
    for j in range(i+1,N+1):
        dfs(j,m-1,nums + [j])

for i in range(1,N+1):
    dfs(i,M,[i])

for answer in answers:
    for i in answer:
        print(i,end=" ")
    print()

