# 킹,퀸 룩, 비숍, 나이트, 폰

import sys

chesses = list(map(int,sys.stdin.readline().split()))

ans = [1,1,2,2,2,8]

for idx,chess in enumerate(chesses):
    ans[idx] = ans[idx] - chess

for i in range(len(ans)):
    print(ans[i],end=" ")

