# [프로그래머스] 이중우선순위큐

import heapq

def solution(operations):
    answer = []
    max_heap,min_heap = [],[]

    for i in range(len(operations)):
        operand,num = operations[i].split()
        if operand == "I":
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))

        elif max_heap and operand == "D" and num == "1":
            heapq.heappop(max_heap)
            min_heap = []
            for j in max_heap:
                heapq.heappush(min_heap, -j)
        elif min_heap and operand == "D" and num == "-1":
            heapq.heappop(min_heap)
            max_heap = []
            for j in min_heap:
                heapq.heappush(max_heap, -j)
    return [max(min_heap) if min_heap else 0,min(min_heap) if min_heap else 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))