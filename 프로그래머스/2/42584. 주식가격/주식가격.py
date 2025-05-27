# [프로그래머스] 주식 가격

def solution(prices):
    result = []
    for i in range(len(prices)):
        temp = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                temp += 1
                break
            else:
                temp +=1
        result.append(temp)
    return result


print(solution([1, 2, 3, 2, 3]))