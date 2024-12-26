# 15649. N과 M (1)

N,M = map(int,input().split())

def dfs(m,nums,visited):
    if m == 1:
        answers.append(nums)
        return

    for j in range(1,N+1):
        if j not in visited:
            dfs(m-1,nums + [j], visited + [j])


answers = []

for i in range(1,N+1):
    dfs(M,[i],[i])

for answer in answers:
    for i in answer:
        print(i,end=" ")
    print()