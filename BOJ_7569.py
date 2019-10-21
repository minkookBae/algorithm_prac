import sys
from collections import deque
from copy import deepcopy

def bfs():
    check = False
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if(my_Map[i][j][k] == 0):
                    check = True
    
    if(not check):
        print(0)
        return

    temp = deepcopy(my_Map)
    q = deque()
    q2 = deque()
    visit_bfs = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if(temp[i][j][k] == 1):
                    q2.append([i,j,k])
    
    q.append(q2)

    while(len(q) > 0):
        current = q.popleft()
        q2 = deque()

        for cur in list(current):
            cur_h = cur[0]
            cur_n = cur[1]
            cur_m = cur[2]

            for dir in range(6):

                n_h = cur_h + dx[dir]
                n_n = cur_n + dy[dir]
                n_m = cur_m + dz[dir]

                if(n_h < 0 or n_h >= H or n_n < 0 or n_n >= N or n_m < 0 or n_m >=M):
                    continue
                    
                if(visit_bfs[n_h][n_n][n_m] == 0 and temp[n_h][n_n][n_m] == 0):
                    visit_bfs[n_h][n_n][n_m] = 1
                    temp[n_h][n_n][n_m] = temp[cur_h][cur_n][cur_m] + 1
                    q2.append([n_h,n_n,n_m])
            
            if(q2 and q2 not in q):
                q.append(q2)

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if(temp[i][j][k] == 0 ):
                    print(-1)
                    return
    
    max_count = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if(max_count < temp[i][j][k]):
                    max_count = temp[i][j][k]
    
    print(max_count-1)
    return


q = lambda : list(map(int,sys.stdin.readline().split()))
M, N, H = q()

my_Map = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        my_Map[i].append(q())

dx, dy ,dz = (1,-1,0,0,0,0), (0,0,1,-1,0,0), (0,0,0,0,1,-1)

bfs()