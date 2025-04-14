# 추억 점수

def solution(name, yearning, photo):
    hash_map = dict()

    for i in range(len(name)):
        hash_map[name[i]] = yearning[i]
    result = []
    for p in photo:
        temp = 0
        for i in p:
            if i in hash_map:
                temp += hash_map[i]
        result.append(temp)
    return result
