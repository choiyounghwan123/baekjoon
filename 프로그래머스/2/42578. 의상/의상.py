# [프로그래머스] 의상.

from collections import defaultdict

def solution(clothes):
    hash_map = defaultdict(int)
    for clothe in clothes:
        hash_map[clothe[1]] += 1
    result = 1
    for key,item in hash_map.items():
        result *= (item + 1)
    return result - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))