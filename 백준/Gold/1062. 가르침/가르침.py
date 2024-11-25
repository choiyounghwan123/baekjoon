# 1062. 가르침
import sys

N,K = map(int,input().split())

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
alphabet = [0] * 26

for c in ['a','n','t','i','c']:
    alphabet[ord(c)- ord('a')] = 1

answer = 0

def dfs(idx, cnt):
    global answer
    if cnt == K - 5:
        count = 0
        for word in words:
            check = True
            for a in word:
                if alphabet[ord(a) - ord("a")] == 0:
                    check = False
                    break
            if check:
                count += 1
        answer = max(answer, count)
        return

    for i in range(idx, 26):
        if not alphabet[i]:
            alphabet[i] = True
            dfs(i,cnt + 1)
            alphabet[i] = False
dfs(0,0)
print(answer)