N = int(input())

nums = list(map(int,input().split()))
total = int(input())

if sum(nums) <= total:
    print(max(nums))
    exit(0)

left,right = 0, 100000

while left <= right:
    middle = (left + right) // 2
    a = total

    for i in range(len(nums)):
        if nums[i] < middle:
            a -= nums[i]
        else:
            a -= middle
    if a < 0:
        right = middle-1
    else:
        left = middle + 1

print(right)