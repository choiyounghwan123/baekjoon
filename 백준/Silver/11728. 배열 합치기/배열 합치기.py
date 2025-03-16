# 11728. 배열 합치기

N,M = map(int, input().split())

def recursive_(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = recursive_(arr[:mid])
    right = recursive_(arr[mid:])
    l,r= 0,0
    new_arr = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new_arr.append(left[l])
            l+=1
        else:
            new_arr.append(right[r])
            r += 1
    new_arr += left[l:]
    new_arr += right[r:]
    return new_arr


arr1 = list(map(int,input().split()))
arr2 = list(map(int, input().split()))
print(*recursive_(arr1 + arr2))