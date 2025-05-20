# [2025 프로그래머스 코드챌린지 1차 예선] 비밀 코드 해독

from itertools import combinations


def solution(n, q, ans):
    num = [i for i in range(1, n + 1)]
    index = list(filter(lambda i: ans[i] == 0, range(len(ans))))

    for i in index:
        for j in q[i]:
            if j in num:
                num.remove(j)
    result = 0
    for i in combinations(num, 5):
        temp = []
        for j in range(len(q)):
            count = 0
            for k in range(5):
                if i[k] in q[j]:
                    count += 1
            temp.append(count)

        for i in range(len(ans)):
            if temp[i] != ans[i]:
                break
        else:
            result +=1
    return result
print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],
               [2, 3, 4, 3, 3]))
