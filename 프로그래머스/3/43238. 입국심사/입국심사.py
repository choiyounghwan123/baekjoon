# [프로그래머스] 입국심사

def solution(n, times):
    left,right = 1, 100000000000000

    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for time in times:
            temp += mid//time
        if temp >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left
print(solution(6,[7,10]))