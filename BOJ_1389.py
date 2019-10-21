import sys
from collections import deque
    
N , M = list(map(int,sys.stdin.readline().split()))
my_Map = [[] for _ in range(N)]

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    for word in temp:
        my_Map[i].append(int(word))

dist = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
dx, dy = (1,-1,0,0) , (0,0,1,-1)

def bfs():
    q = deque()
    q.append([0,0,0])
    dist[0][0][0] = 1

    while(len(q) > 0):
        current = q.popleft()
        x, y, wall = current[0], current[1], current[2]

        if(x == N-1 and y == M -1 ):
            return dist[x][y][wall]

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue
            
            if(dist[nx][ny][wall]):
                continue
            
            if(my_Map[nx][ny] == 0):
                dist[nx][ny][wall] = dist[x][y][wall] + 1
                q.append([nx,ny,wall])
            
            if(my_Map[nx][ny] == 1 and wall == 0):
                dist[nx][ny][1] = dist[x][y][wall] + 1
                q.append([nx,ny,1])
    
    return -1

print(bfs())

# https://rebas.kr/658 참고