# [PCCP] 1. 붕대감기

def solution(bandage, health, attacks):
    current_health = health
    j = 0
    consecutiveSuccessCount = 0
    for i in range(attacks[-1][0]+1):
        if attacks[j][0] == i:
            print("1")
            consecutiveSuccessCount = 0
            current_health -= attacks[j][1]
            j+=1
            if current_health <= 0:
                return -1
        else:
            current_health += bandage[1]
            consecutiveSuccessCount += 1
            if consecutiveSuccessCount == bandage[0]:
                current_health += bandage[2]
                consecutiveSuccessCount = 0
            if current_health > health:
                current_health = health
    return current_health

print(solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))