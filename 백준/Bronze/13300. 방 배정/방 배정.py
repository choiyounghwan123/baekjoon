N,K = map(int,input().split())

nums1 = [0] * (7)
nums2 = [0] * (7)
total = 0
for i in range(N):
    S,Y = map(int,input().split())

    if S == 0:
        nums1[Y] +=1
        if nums1[Y] == 1:
            total +=1
        if nums1[Y] == K:
            nums1[Y] = 0
    else:
        nums2[Y] +=1
        if nums2[Y] == 1:
            total +=1
        if nums2[Y] == K:
            nums2[Y] = 0


print(total)