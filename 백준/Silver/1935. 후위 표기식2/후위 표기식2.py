# 1935. 후위 표기식 2

N = int(input())
postfix_notation = input()

result = 0
stack = []
nums = []

for _ in range(N):
    nums.append(int(input()))

for postfix in postfix_notation:
    if postfix == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif postfix == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif postfix == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif postfix == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else:
        stack.append(nums[ord(postfix) - ord("A")])

print(f"{stack[-1]:.2f}")