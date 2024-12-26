# 15654. N과 M (5)

N,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answers = []

def dfs(m,answer):
    if m == 1:
        answers.append(answer)
        return

    for num in nums:
        if num not in answer:
            dfs(m-1,answer + [num])

for num in nums:
    dfs(M,[num])

for answer in answers:
    for i in answer:
        print(i,end=" ")
    print()