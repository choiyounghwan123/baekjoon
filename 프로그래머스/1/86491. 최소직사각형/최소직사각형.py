# [프로그래머스] 최소직사각형

def solution(sizes):
    arr1 = []
    arr2 = []
    for size in sizes:
        arr1.append(max(size))
        arr2.append(min(size))
    return max(arr1) * max(arr2)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))