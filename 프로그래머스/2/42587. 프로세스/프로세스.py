# [프로그래머스] 프로세스

from collections import deque

def solution(priorities, location):
    queue = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)
    answer = 0
    while queue:
        if priorities[0] < max(priorities):
            priorities.append(priorities.popleft())
            queue.append(queue.popleft())
            continue
        priorities.popleft()
        answer +=1
        if queue.popleft() == location:
            return answer


print(solution([2, 1, 3, 2],2))