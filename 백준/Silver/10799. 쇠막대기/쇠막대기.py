# 10799. 쇠막대기

bar = list(input().rstrip())

stack = []
result = 0
for i in range(len(bar)):
    if bar[i] == "(":
        stack.append(bar[i])
    elif stack and stack[-1] == "(" and bar[i] == ")" and bar[i-1] == "(":
        stack.pop()
        result+= len(stack)
    else:
        stack.pop()
        result+=1
print(result)