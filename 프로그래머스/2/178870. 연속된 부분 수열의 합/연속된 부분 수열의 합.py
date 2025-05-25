# [프로그래머스] 연속된 부분 수열의 합

def solution(sequence, k):
    left,right =0,1
    answer = [0,1000000000]
    prefix_sum = [0]
    for num in sequence:
        prefix_sum.append(prefix_sum[-1] + num)
    while right < len(prefix_sum):
        if prefix_sum[right] - prefix_sum[left] < k:
            right +=1
        elif prefix_sum[right] - prefix_sum[left] > k:
            left +=1
        else:
            if answer[1] - answer[0] > right - left:
                answer = [left,right]
            right += 1
    return [answer[0],answer[1]-1]

print(solution([1, 1, 1, 2, 3, 4, 5]	,5))