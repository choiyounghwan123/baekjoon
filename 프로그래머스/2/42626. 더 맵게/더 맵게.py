# [프로그래머스] 더 맵게

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    try:
        while scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + (b*2))
            answer += 1
        return answer
    except:
        return -1

print(solution([1, 2, 3, 9, 10, 12],0))