q = lambda : list(map(int,input().split()))

N, M = q()
x, y, dir = q()

my_Map = []
for _ in range(N):
    my_Map.append(q())

dx, dy = (-1,0,1,0), (0,1,0,-1)

my_Map[x][y] = 2
res = 1

while(True):
    c = False
    for _ in range(4):
        next_dir = (dir+3) % 4
        next_x , next_y = x+dx[next_dir], y+dy[next_dir]
        dir = next_dir

        if(my_Map[next_x][next_y] == 0):
            my_Map[next_x][next_y] = 2
            res += 1
            c = True
            x, y = next_x, next_y
            break

    if not c:
        if(my_Map[x+dx[(dir+2)%4]][y+dy[(dir+2)%4]] == 1):
            break
        else:
            x, y = x+dx[(dir+2)%4], y+dy[(dir+2)%4]
    

print(res)