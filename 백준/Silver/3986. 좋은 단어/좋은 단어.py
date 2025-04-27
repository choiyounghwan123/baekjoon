# 3986. 좋은 단어
result = 0
for _ in range(int(input())):
    word = input()
    stack = []

    for s in word:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        result+=1
print(result)