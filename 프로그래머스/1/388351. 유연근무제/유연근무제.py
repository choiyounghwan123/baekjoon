# [2025 프로그래머스 코드챌린지 1차 예선] 유연근무제

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        day = startday
        hope_start_time = schedules[i]+10
        print(hope_start_time)
        a = str(hope_start_time)
        if int(a[-2] + a[1]) >= 60:
            hope_start_time = hope_start_time + 100 - 60
        print(hope_start_time)
        for j in range(len(timelogs[i])):
            if day > 5:
                if day == 7:
                    day = 1
                    continue
                day += 1
                continue
            if timelogs[i][j] > hope_start_time:
                break
            day = (day) % 7 + 1
        else:
            answer += 1
    return answer

print(solution([755, 800, 1100],[[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]],5))