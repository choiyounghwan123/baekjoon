import sys

nums = list(map(int,sys.stdin.readline().split()))
check = 0
if nums[0] == 1:
    for i in range(1,8):
        if nums[i] == i+1:
            check = 1
        else:
            check = 0
            break
    if check:
        print("ascending")
    else:
        print("mixed")
elif nums[0] == 8:
    for i in range(1,8):
        if nums[i] == 8-i:
            check = 1
        else:
            check = 0
            break
    if check:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")