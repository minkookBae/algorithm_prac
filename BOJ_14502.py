def dfs(count, x, y):
    if(count == 3):
        bfs()
        return
    
    for i in range(x,N):
        for j in range(y,M):
            if(my_map[i][j] == 0):
                my_map[i][j] = 1
                dfs(count+1, i, j)
                my_map[i][j] = 0
        
        y = 0

def bfs():
    global answer

    temp = [[0 for _ in range(M)] for _ in range(N)]
    queue = []
    visit = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            temp[i][j] = my_map[i][j]

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 2):
                queue.append([i,j])
                visit[i][j] = 1

    while(len(queue) != 0):
        current = queue.pop(0)
        
        cur_x, cur_y  = current[0], current[1]

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue
            
            if(visit[nx][ny] == 0 and temp[nx][ny] == 0):
                temp[nx][ny] = 2
                visit[nx][ny] = 1
                queue.append([nx,ny])

    sum = 0

    for i in range(N):
        for j in range(M):
            if(temp[i][j] == 0):
                sum += 1

    answer = max(answer, sum)


if __name__ == "__main__":
    
    q = lambda : list(map(int,input().split()))

    N, M = q()
    my_map = []

    for _ in range(N):
        my_map.append(q())

    dx, dy = [-1,1,0,0], [0,0,-1,1] # 상,하,좌,우

    answer = 0

    dfs(0,0,0)
    print(answer)