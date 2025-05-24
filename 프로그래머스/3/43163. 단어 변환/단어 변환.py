# [프로그래머스] 단어 변환

from collections import deque

def solution(begin, target, words):
    visited = [begin]
    queue = deque([[begin,0]])
    while queue:
        vertex,count = queue.popleft()

        if vertex == target:
            return count
        for i in range(len(vertex)):
            for j in range(26):
                next_char = chr(ord('a') + j)
                if next_char == vertex[i]:
                    continue
                new_word = vertex[:i] + next_char + vertex[i+1:]
                if new_word in words and new_word not in visited:
                    visited.append(new_word)
                    queue.append([new_word,count + 1])
    return 0



print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))