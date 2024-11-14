# 1316. 그룹 단어 체커

N = int(input())

result = 0

for _ in range(N):
    word = input().rstrip()
    set_ = set()
    pre = None
    check = True

    for i in range(len(word)-1):
        if word[i] in set_ or word[i+1] in set_:
            check = False
            break
        elif word[i] == word[i+1]:
            continue
        else:
            set_.add(word[i])

    if check:
        result += 1
print(result)
