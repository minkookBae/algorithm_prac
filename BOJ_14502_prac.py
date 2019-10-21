from copy import deepcopy

def dfs(count , x , y):
    if(count == 3):
        bfs()
        return
    
    for i in range(x,N):
        for j in range(y,M):
            if(my_Map[i][j] == 0):
                my_Map[i][j] = 1
                dfs(count+1, i, j)
                my_Map[i][j] = 0

        y = 0

def bfs():
    global answer
    temp = deepcopy(my_Map)
    queue = []
    visit = [[0 for i in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 2):
                queue.append([i,j])
                visit[i][j] = 1

    while(len(queue) != 0):
        current = queue.pop(0)
        cur_x , cur_y = current[0], current[1]

        for i in range(4):
            next_x , next_y = cur_x + dx[i], cur_y + dy[i]

            if(next_x < 0 or next_y < 0 or next_x >= N or next_y >= M):
                continue
            
            if(temp[next_x][next_y] == 0 and visit[next_x][next_y] == 0):
                temp[next_x][next_y] = 2
                visit[next_x][next_y] = 1
                queue.append([next_x,next_y])
    
    sum = 0

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 0):
                sum += 1

    
    answer = max(answer, sum)


q = lambda : list(map(int,input().split()))

N, M = q()
my_Map = []

for _ in range(N):
    my_Map.append(q())

dx, dy = [-1,0,1,0], [0,1,0,-1] # 북, 동, 남, 서
answer = 0

dfs(0,0,0)
print(answer)