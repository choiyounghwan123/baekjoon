import sys

nums = list(sys.stdin.readline().rstrip() for _ in range(3))

print(int(nums[0]) + int(nums[1]) - int(nums[2]))
print(int(nums[0] + nums[1]) - int(nums[2]))