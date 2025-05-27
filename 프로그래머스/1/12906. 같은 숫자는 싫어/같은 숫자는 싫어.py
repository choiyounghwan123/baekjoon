# [프로그래머스] 같은 숫자는 싫어.

def solution(arr):
    answer = [arr[0]]
    for element in arr:
        if answer[-1] == element:
            continue
        else:
            answer.append(element)
    return answer

print(solution([1,1,3,3,0,1,1]))