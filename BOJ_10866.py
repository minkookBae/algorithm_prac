import sys
from collections import deque

class Deque:

    def __init__(self):
        self._deque = deque()

    def push_front(self,x):
        self._deque.appendleft(x)
    
    def push_back(self,x):
        self._deque.append(x)

    def pop_front(self):
        if(len(self._deque) > 0):
            print(self._deque.popleft())
        else:
            print(-1)

    def pop_back(self):
        if(len(self._deque) > 0):
            print(self._deque.pop())
        else:
            print(-1)
    
    def size(self):
        print(len(self._deque))

    def empty(self):
        if(len(self._deque) == 0):
            print(1)
        else:
            print(0)
    
    def front(self):
        if(len(self._deque) == 0):
            print(-1)
        else:
            print(self._deque[0])
    
    def back(self):
        if(len(self._deque) == 0):
            print(-1)
        else:
            print(self._deque[-1])
    
    
N = int(sys.stdin.readline())

q = Deque()

for _ in range(N):
    
    order = sys.stdin.readline().split()

    if(order[0] == "push_front"):
        q.push_front(order[1])

    elif(order[0] == "push_back"):
        q.push_back(order[1])
    
    elif(order[0] == "pop_front"):
        q.pop_front()
    
    elif(order[0] == "pop_back"):
        q.pop_back()
    
    elif(order[0] == "size"):
        q.size()
    
    elif(order[0] == "empty"):
        q.empty()
    
    elif(order[0] == "front"):
        q.front()
    
    elif(order[0] == "back"):
        q.back()
    