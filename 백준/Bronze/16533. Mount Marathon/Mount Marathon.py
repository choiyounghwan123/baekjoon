# 1503. Mount Marathon

N = int(input())
cards = list(map(int,input().split()))
result = 0
stack = [cards[-1]]
for i in range(N-2,-1,-1):
    if stack[-1] <= cards[i]:
        stack.append(cards[i])
    else:
        result+=1
        stack = [cards[i]]
print(result + 1 if stack else result)