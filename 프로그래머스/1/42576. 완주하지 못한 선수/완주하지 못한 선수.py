# [프로그래머스] 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    counter = Counter(completion)

    for p in participant:
        if p not in counter:
            return p
        else:
            counter[p] -=1
            if counter[p] == 0:
                del counter[p]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))