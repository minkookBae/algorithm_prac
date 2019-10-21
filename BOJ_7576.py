import sys
from copy import deepcopy

def bfs():
    global answer
    temp = deepcopy(my_Map)
    visit_bfs = [[0 for _ in range(M)] for _ in range(N)]
    q = []
    q2 = []
    count = 0
    changed = False

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 1):
                q2.append([i,j])
                visit_bfs[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            if(temp[i][j] == -1):
                visit_bfs[i][j] = 1

    if(q2):
        q.append(q2)

    if(not q):
        print(-1)
        return

    while(len(q) > 0):
        current_q = q.pop(0)
        next_q = []
        count += 1

        for cur in current_q:
            
            cur_x = cur[0]
            cur_y = cur[1]
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                    continue
                
                if(temp[nx][ny] == 0 and visit_bfs[nx][ny] == 0):
                    visit_bfs[nx][ny] = 1
                    temp[nx][ny] = count
                    next_q.append([nx,ny])
            if(next_q and next_q not in q):
                q.append(next_q)
                changed = True

                
    max_num = 0
    for i in range(N):
        for j in range(M):
            if(max_num < temp[i][j]):
                max_num = temp[i][j]
    
    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 0):
                print(-1)
                return


    if(changed):
        print(max_num)
    else:
        print(0)
        
    return

q = lambda : list(map(int,sys.stdin.readline().split()))

M, N = q()
my_Map = []
for _ in range(N):
    my_Map.append(q())


dx, dy = (-1,0,1,0) , (0,1,0,-1)
answer = 0

bfs()