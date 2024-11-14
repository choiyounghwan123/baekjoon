# 10815.

N = int(input())
nums_one = list(map(int,input().split()))
M= int(input())
nums_two = list(map(int,input().split()))
nums_one.sort()
for num in nums_two:
    start,end = 0, N - 1
    check = 0
    while start <= end:
        mid = (start + end) // 2
        if nums_one[mid] < num:
            start = mid + 1
        elif nums_one[mid] > num:
            end = mid - 1
        else:
            check = 1
            break
    if check:
        print(1,end=" ")
    else:
        print(0,end=" ")