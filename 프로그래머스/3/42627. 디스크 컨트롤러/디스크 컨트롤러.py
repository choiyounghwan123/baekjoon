# [프로그래머스] 디스크 컨트롤러

import heapq

def solution(jobs):
    t = 0
    jobs.sort(key=lambda x:[x[0],x[1]])
    queue = []
    current = []
    result = []
    while jobs or queue or current:
        if current and current[0] == t:
            current = []
        while jobs and jobs[0][0] == t:
            a = jobs.pop(0)
            heapq.heappush(queue, [a[1],a[0]])
        if queue and not current:
            a = heapq.heappop(queue)
            current = [t+a[0],a[1]]
            result.append(t + a[0] - a[1])


        t += 1
    return sum(result) // len(result)




print(solution([[0, 3], [0,1],[0,4],[1, 9],[1,4], [3, 5],[5,1],[1,10],[1,1000],[100,10]]))