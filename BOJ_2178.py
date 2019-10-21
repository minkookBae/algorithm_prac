import sys
from collections import deque
from copy import deepcopy

def bfs():
    visit_bfs = [[0 for _ in range(M)] for _ in range(N)]
    visit_bfs[0][0] = 1

    q = deque()
    q.append([0,0])
    while(q):
        current = q.popleft()
        cur_x = current[0]
        cur_y = current[1]

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue
                
            if(visit_bfs[nx][ny] == 0 and temp[nx][ny] == 1):
                visit_bfs[nx][ny] = 1
                temp[nx][ny] = temp[cur_x][cur_y] + 1
                q.append([nx,ny])  
    
    print(temp[N-1][M-1])
    


N, M = list(map(int,sys.stdin.readline().split()))
my_Map = [[] for _ in range(N)]

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    for word in temp:
        my_Map[i].append(int(word))

dx, dy = (-1,1,0,0), (0,0,-1,1)
answer = 0
result = []
temp = deepcopy(my_Map)


bfs()