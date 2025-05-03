# PCCP 2. 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    left,right = 0, 300000
    result = 10 ** 15
    while left <= right:
        level = (left+right) // 2
        print(level)
        total = times[0]
        for i in range(1,len(diffs)):
            if diffs[i] > level:
                total += (diffs[i] - level) * (times[i-1] + times[i]) + times[i]
            else:
                total += times[i]
        if total > limit:
            left = level + 1
        else:
            right = level - 1
            result = min(result,level)
            result = max(1,result)
    return result

print(solution([1, 1, 1],[1, 1,1],59))