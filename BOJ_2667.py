import sys

def dfs(cur_x,cur_y):
    global count
    my_Map[cur_x][cur_y] = '0'
    count += 1

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if(nx < 0 or nx >= N or ny < 0 or ny >= N):
            continue

        if(my_Map[nx][ny] == '1'):
            dfs(nx,ny)


N = int(sys.stdin.readline())
my_Map = [[] for _ in range(N)]
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    for word in temp:
        my_Map[i].append(word)

dx, dy = (1,-1,0,0), (0,0,1,-1)
result = []

for i in range(N):
    for j in range(N):
        if(my_Map[i][j] == '1'):
            count = 0
            dfs(i,j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)