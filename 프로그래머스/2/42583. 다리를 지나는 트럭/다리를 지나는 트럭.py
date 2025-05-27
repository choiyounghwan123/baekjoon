# [프로그래머스] 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([])
    result = 1
    weight1 = deque([])
    while truck_weights or queue:
        if truck_weights and sum(weight1) + truck_weights[0] <= weight:
            queue.append(bridge_length)
            weight1.append(truck_weights.pop(0))
        for i in range(len(queue)):
            queue[i] -= 1
        if queue[0] == 0:
            queue.popleft()
            weight1.popleft()
        result += 1
    return result

print(solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))