# [프로그래머스] 카펫

def solution(brown, yellow):
    temp = 0
    i = 1
    a = 0
    while temp != brown:
        if yellow % i != 0:
            i+=1
            continue
        a = yellow // i
        temp = (a + 2) * 2 + i*2
        i+=1
    return [a+2,i+1]

print(solution(24,24))