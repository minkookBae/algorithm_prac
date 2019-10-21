import sys

class Queue:

    def __init__(self):
        self._queue = []
    
    def push(self, x):
        self._queue.append(x)
    
    def pop(self):
        if(len(self._queue)>0):
            print(self._queue.pop(0))
        else:
            print(-1)
    
    def size(self):
        print(len(self._queue))
    
    def empty(self):
        if(len(self._queue) > 0):
            print(0)
        else:
            print(1)

    def front(self):
        if(len(self._queue) == 0):
            print(-1)
        else:
            print(self._queue[0])
    
    def back(self):
        if(len(self._queue) == 0):
            print(-1)
        else:
            print(self._queue[-1])
    
    



N = int(sys.stdin.readline())

queue = Queue()

for _ in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == "push"):
        queue.push(int(order[1]))
    elif(order[0] == "pop"):
        queue.pop()
    elif(order[0] == "size"):
        queue.size()
    elif(order[0] == "empty"):
        queue.empty()
    elif(order[0] == "front"):
        queue.front()
    elif(order[0] == "back"):
        queue.back()
    