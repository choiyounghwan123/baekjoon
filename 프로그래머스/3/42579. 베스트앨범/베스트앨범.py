# [프로그래머스] 베스트앨범
from collections import defaultdict

def solution(genres, plays):
    hash_map = defaultdict(list)
    hash_map1 = defaultdict(int)
    answer = []
    i = 0
    for genre,play in zip(genres,plays):
        hash_map[genre].append([play,i])
        hash_map1[genre] += play
        i+=1
    a = sorted(hash_map1.items(), key=lambda x: x[1])
    for i in range(len(a)):
        genre = a[-1 - i][0]
        hash_map[genre].sort(key=lambda x:(x[0],-x[1]))
        print(hash_map)
        print(hash_map[genre])
        j = 0
        while j < 2 and hash_map[genre]:
            answer.append(hash_map[genre].pop(-1)[1])
            j+=1
    return answer

print(solution(["classic","classic","classic"], [500,500,500]))