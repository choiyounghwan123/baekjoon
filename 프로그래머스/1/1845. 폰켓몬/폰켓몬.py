# [프로그래머스] 포켓몬
from collections import Counter


def solution(nums):
    answer = 0
    counter = Counter(nums)
    target = len(nums) // 2
    arr = set()
    while target > 0:
        for key,item in counter.items():
            arr.add(key)
            counter[key] -=1
            target -= 1
            if target <= 0:
                break


    return len(arr)

print(solution([3,1,2,3]))