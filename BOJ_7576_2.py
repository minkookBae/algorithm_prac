import sys
from collections import deque
from copy import deepcopy

def bfs():
    check = False
    for i in range(N):
        for j in range(M):
            if(my_Map[i][j] == 0):
                check = True
    
    if(not check):
        print(0)
        return
    
    visit_bfs = [[0 for _ in range(M)] for _ in range(N)]
    temp = deepcopy(my_Map)
    q = deque()
    q2 = deque()

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 1):
                q2.append([i,j])
                visit_bfs[i][j] = 1
    q.append(q2)
    
    while(len(q) > 0):
        q2 = deque()
        current_q = q.popleft()

        for cur in current_q:
            cur_x = cur[0]
            cur_y = cur[1]

            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                    continue
                
                if(visit_bfs[nx][ny] == 0 and temp[nx][ny] == 0):
                    q2.append([nx,ny])
                    temp[nx][ny] = temp[cur_x][cur_y] + 1
                    visit_bfs[nx][ny] = 1
            if(q2 and q2 not in q):
                q.append(q2)
    
    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 0):
                print(-1)
                return
    
    max_num = 0

    for i in range(N):
        for j in range(M):
            if(max_num < temp[i][j]):
                max_num = temp[i][j]
    
    print(max_num-1)
    return
            


q = lambda : list(map(int,sys.stdin.readline().split()))

M, N = q()
my_Map = []

for _ in range(N):
    my_Map.append(q())

dx, dy = (-1,1,0,0) , (0,0,-1,1)
bfs()