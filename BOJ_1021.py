import sys
from collections import deque

N , M = list(map(int,sys.stdin.readline().split()))
q = deque(list(map(int,sys.stdin.readline().split())))

target_q = deque()

for i in range(1,N+1):
    target_q.append(i)

count = 0

while(len(q) > 0):
    
    if(q[0] == target_q[0]):
        target_q.popleft()
        q.popleft()
    
    else:
        if(target_q.index(q[0]) > len(target_q)//2):
            idx = len(target_q) - target_q.index(q[0])
            for _ in range(idx):
                target_q.appendleft(target_q.pop())
                count += 1
        
        else:
            idx = target_q.index(q[0])
            for _ in range(idx):
                target_q.append(target_q.popleft())
                count += 1

print(count)