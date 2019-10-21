def solve(x, y, dir, ans):
    while(True):
        # 4번 회전
        c = False
        for i in range(4):
            next_dir = (dir+3) % 4 # 시작하자마자 왼쪽부터 회전
            next_x , next_y = x + dx[next_dir], y + dy[next_dir]
            # 전진
            dir = next_dir

            if(my_Map[next_x][next_y] == 0):
                c = True
                my_Map[next_x][next_y] = 2
                ans += 1
                x, y = next_x, next_y
                break
        
        if not c:
            if(my_Map[x+dx[(dir+2)%4]][y+dy[(dir+2)%4]] == 1):
                return ans
            else:
                x, y = x+dx[(dir+2)%4], y+dy[(dir+2)%4]


N, M = map(int,input().split())
r, c, d = list(map(int,input().split()))

my_Map = []
for _ in range(N):
    my_Map.append(list(map(int,input().split())))

# 맵 만들기

dx, dy = (-1,0,1,0), (0,1,0,-1)

my_Map[r][c] = 2

print(solve(r,c,d,1))

