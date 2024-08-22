# 스택

import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("-1")
        else:
            print(self.stack.pop())
            self.size -= 1

    def size1(self):
        print(self.size)

    def top(self):
        if self.size == 0:
            print("-1")
        else:
            print(self.stack[-1])
    def empty(self):
        if self.size == 0:
            print(1)
        else:
            print(0)

stack = Stack()

for _ in range(int(sys.stdin.readline())):
    order = list(map(str,sys.stdin.readline().rstrip().split()))

    if len(order) == 1:
        if order[0] == "top":
            stack.top()
        elif order[0] == "pop":
            stack.pop()
        elif order[0] == "size":
            stack.size1()
        else:
            stack.empty()
    else:
        stack.push(order[1])


