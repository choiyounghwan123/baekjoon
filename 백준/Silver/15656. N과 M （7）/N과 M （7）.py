# 15656. N과 M (7)

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answers = []

def dfs(m,answer):
    if m == 1:
        answers.append(answer)
        return

    for i in range(N):
        dfs(m-1,answer + [nums[i]])
for i in range(N):
    dfs(M,[nums[i]])

for answer in answers:
    for i in answer:
        print(i,end=" ")
    print()


