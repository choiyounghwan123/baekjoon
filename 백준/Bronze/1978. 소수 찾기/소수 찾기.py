import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
check = 0
result = 0

for i in range(N):
    check = 0
    if nums[i] == 1:
        continue
    for j in range(2,nums[i]):
        if nums[i]%j == 0:
            check = 1
            break
    if not check:
        result+=1

print(result)