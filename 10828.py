import sys


class Stack:
    def __init__(self):
        self.data = []  # data 라는 맴버변수에 빈 리스트를 생성

    def __len__(self):
        return len(self.data)  # data 라는 리스트 변수에 저장된 요소의 개수를 반환

    def push(self, n):
        self.data.append(n)

    def isEmpty(self):
        return int(len(self.data) == 0)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.data[-1]


stack = Stack()

N = int(sys.stdin.readline())

for i in range(N):
    order = list(sys.stdin.readline())

    if order[0] == "push":
        stack.push(int(order[1]))
    elif order[0] == "pop":
        print(stack.pop())
    elif order[0] == "size":
        print(stack.__len__())
    elif order[0] == "empty":
        print(stack.isEmpty())
    elif order[0] == "top":
        print(stack.top())
