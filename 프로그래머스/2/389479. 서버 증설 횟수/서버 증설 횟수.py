# [2025 프로그래머스 코드챌린지 2차 예선] 서버 증설 횟수

def solution(players, m, k):
    current_server = 0
    timer = []
    a = []
    result = 0
    for i in range(len(players)):
        print(a,timer)
        if timer:
            idx = []
            for j in range(len(timer)):
                timer[j] -= 1
                if timer[j] == 0:
                    idx.append(j)
                    current_server -= a[j]
            for index in idx:
                timer.pop(index)
                a.pop(index)
        if players[i] >= (current_server + 1) * m:
            a.append(players[i] // m - current_server)
            result += a[-1]
            current_server += a[-1]
            timer.append(k)
            print(current_server)
    return result


print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],3,5))