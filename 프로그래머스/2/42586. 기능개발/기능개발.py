# [프로그래머스] 기능개발
def solution(progresses, speeds):
    answer = []
    i = 0
    while i < len(progresses):
        for j in range(len(progresses)):
            progresses[j] += speeds[j]
        temp = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            temp +=1
        if temp:
            answer.append(temp)

    return answer
print(solution([93, 30, 55],[1,30,5]))