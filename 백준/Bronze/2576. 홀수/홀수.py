import sys

nums = []

for i in range(7):
    x = int(sys.stdin.readline())

    if x % 2 == 1:
        nums.append(x)

if len(nums) == 0:
    print("-1")
else:
    print(sum(nums))
    print(min(nums))