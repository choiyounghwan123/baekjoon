# [프로그래머스] 과일장수

import heapq

def solution(k, m, score):
    answer = 0

    score.sort()
    while len(score) >= m:
        temp = []
        for i in range(m):
            temp.append(score.pop(-1))
        answer += min(temp) * m
    return answer

print(solution(4,2,[1,2,3,2,2,2,1,4,5,6]))