# 귤 고르기

import heapq
from collections import defaultdict
def solution(k, tangerine):
    hash_map = defaultdict(int)
    arr = []
    for t in tangerine:
        hash_map[t] += 1
    for key,item in hash_map.items():
        arr.append(item)
    arr.sort(reverse=True)
    result = 0
    temp = 0
    for element in arr:
        if temp + element <= k:
            temp +=element
            result+=1
            if temp == k:
                break
        else:
            result +=1
            temp += element
            break
    return result



print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))