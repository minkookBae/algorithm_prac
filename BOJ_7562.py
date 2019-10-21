import sys
from collections import deque

def bfs():
    visit_bfs[now_x][now_y] = 1
    q = deque()
    q.append([now_x, now_y,0])

    if(now_x == target_x and now_y == target_y):
        print(0)
        return

    while(len(q) > 0):
        current = q.popleft()

        cur_x = current[0]
        cur_y = current[1]
        cur_count = current[2]

        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if(nx < 0 or nx >= I or ny < 0 or ny >= I):
                continue

            if(nx == target_x and ny == target_y):
                print(cur_count + 1)
                return
            
            if(visit_bfs[nx][ny] == 0 and my_Map[nx][ny] == 0):
                visit_bfs[nx][ny] = 1
                q.append([nx,ny,cur_count+1])


T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    I = int(sys.stdin.readline())

    now_x, now_y = list(map(int,sys.stdin.readline().split()))
    target_x , target_y = list(map(int,sys.stdin.readline().split()))

    dx, dy  = (-2, -1, 1, 2, -2, -1, 1, 2), (1, 2, 2, 1, -1, -2, -2, -1)

    my_Map = [[0 for _ in range(I)] for _ in range(I)]
    visit_bfs = [[0 for _ in range(I)] for _ in range(I)]
    my_Map[now_x][now_y] = 1

    bfs()