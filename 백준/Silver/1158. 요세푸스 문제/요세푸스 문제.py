# 1158. 요세푸스 문제

import collections

N,K = map(int,input().split())

queue = collections.deque([i for i in range(1,N+1)])
result = []

while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<",end="")
for i in range(len(result)):
    if len(result)-1 == i:
        print(result[i],end=">")
        break
    print(result[i],end=", ")
