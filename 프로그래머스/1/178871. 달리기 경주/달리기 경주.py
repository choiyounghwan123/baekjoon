def solution(players, callings):
    hash_map = dict()

    for i in range(len(players)):
        hash_map[players[i]] = i

    for i in range(len(callings)):
        index = hash_map[callings[i]]
        index_ = players[index - 1]
        players[index],players[index - 1] = players[index-1], players[index]
        hash_map[callings[i]] -= 1
        hash_map[index_] += 1

    return players