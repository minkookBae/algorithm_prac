import sys

class Stack:

    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)
    
    def pop(self):
        if(len(self._stack) == 0):
            return -1
        else:
            ret = self._stack[-1]
            self._stack = self._stack[:-1]
            return ret
    
    def size(self):
        return len(self._stack)

    def empty(self):
        if(len(self._stack) == 0):
            return 1   
        else : return 0

    def top(self):
        if(len(self._stack) == 0):
            return -1
        else:
            return self._stack[-1]

N = int(sys.stdin.readline())

stack = Stack()

for _ in range(N):

    order = sys.stdin.readline().split()
    if(order[0] == "push"):
        stack.push(order[1])
    elif(order[0] == "pop"):
        print(stack.pop())
    elif(order[0] == "size"):
        print(stack.size())
    elif(order[0] == "empty"):
        print(stack.empty())
    elif(order[0] == "top"):
        print(stack.top())
