# [프로그래머스] H-Index

def solution(citations):
    citations.sort()
    left,right = 0,citations[-1]

    while left<=right:
        mid = (left + right) // 2
        print(mid)
        temp = 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                temp +=1
        if temp >= mid:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(solution([3,3,3,4]))

# 0 1 2 3 4
# 5 - 1