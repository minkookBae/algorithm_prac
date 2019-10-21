import sys
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    q2 = deque()
    q2.append(q)
    visit = [0 for _ in range(100002)]
    visit[N] = 1
    while(len(q2) > 0):
        current = q2.popleft()
        q3 = deque()
        for move in current:
            
            # 오른쪽이동
            if((move+1 <= K+1) and visit[move+1] == 0 or my_Map[move+1] > my_Map[move] + 1):
                visit[move+1] = 1
                my_Map[move+1] = my_Map[move] + 1
                q3.append(move+1)
            
            # 왼쪽 이동
            if((move-1 > 0) and visit[move-1] == 0 or my_Map[move-1] > my_Map[move] + 1):
                visit[move-1] = 1
                my_Map[move-1] = my_Map[move] + 1
                q3.append(move-1)
            
            # 곱하기 2 이동
            if((move*2 <= K+1) and visit[move*2] == 0 or my_Map[move*2] > my_Map[move] + 1):
                visit[move*2] = 1
                my_Map[move*2] = my_Map[move] + 1
                q3.append(move*2)
        if(q3 and q3 not in q2):
            q2.append(q3)
    print(my_Map[0:K+1])
    print(my_Map[K])

N, K = list(map(int,sys.stdin.readline().split()))
my_Map = [0 for _ in range(100002)]


bfs()