def solution(s):
    answer = []
    hash_map = dict()

    for i in range(len(s)):
        if s[i] in hash_map:
            answer.append(i - hash_map[s[i]])
            hash_map[s[i]] = i
            continue
        hash_map[s[i]] = i
        answer.append(-1)

    return answer

print(solution("banana"))