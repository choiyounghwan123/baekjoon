# [프로그래머스] 신고 결과 받기

from collections import defaultdict

def solution(id_list, report, k):
    hash_map = defaultdict(set)
    answer =  [0] * len(id_list)
    for i in range(len(report)):
        reporter,reportedUser = report[i].split(" ")
        hash_map[reportedUser].add(reporter)
    for key,item in hash_map.items():
        item = list(item)
        if len(item) >= k:
            for i in range(len(item)):
                answer[id_list.index(item[i])] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))