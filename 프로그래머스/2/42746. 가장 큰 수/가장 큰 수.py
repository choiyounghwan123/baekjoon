# [프로그래머스] 가장 큰 수

def solution(numbers):
    number = list(map(str, numbers))
    number.sort(key= lambda x: x*3, reverse=True)
    return str(int("".join(number)))

print(solution([6, 10, 2]))