# [프로그래머스] 모의고사

def solution(answers):
    result = [0,0,0]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            result[0] += 1
        if b[i%8] == answers[i]:
            result[1] +=1
        if c[i%10] == answers[i]:
            result[2] +=1
    max_ = max(result)
    d = []
    for i in range(3):
        if max_ == result[i]:
            d.append(i+1)
    return d

print(solution([1,2,3,4,5]))
