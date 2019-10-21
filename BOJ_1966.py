import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = list(map(int,sys.stdin.readline().split()))

    q = deque()
    q2 = deque()
    L = list(map(int,sys.stdin.readline().split()))
    
    for i in L:
        q.append(i)
        q2.append(0)

    q2[M] = 1
    order = 1
    count = 0

    if(N == 1):
        print(1)

    else:
        while(len(q) > 0):
            temp = q[0]

            if(temp < max(q)):
                q.append(q.popleft())
                q2.append(q2.popleft())

            else:
                order_temp = q2.popleft()
                q.popleft() # 출력
                count += 1
                if(order_temp == 1):
                    print(count)
