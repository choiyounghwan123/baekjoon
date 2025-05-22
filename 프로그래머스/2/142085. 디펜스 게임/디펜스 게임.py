# [프로그래머스] 디펜스 게임

import heapq
def solution(n, k, enemy):
    heap = []
    sum_enemy,result = 0,0
    for e in enemy:
        result += 1
        heapq.heappush(heap, -e)
        sum_enemy += e
        if sum_enemy > n:
            if not k: 
                result -=1 
                break
            while k and sum_enemy > n:
                sum_enemy += heapq.heappop(heap)
                k-=1

    print(sum_enemy)
    return result


print(solution(7,3, [4, 2, 4, 5, 3, 3, 1]))