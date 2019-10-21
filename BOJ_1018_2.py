import sys

N, M = list(map(int,sys.stdin.readline().split()))
my_Map = [[] for _ in range(N)]

for i in range(N):
    temp = sys.stdin.readline().strip()
    for alpha in temp:
        my_Map[i].append(alpha)

color_list = ["B", "W"]

min_count = 100000

for i in range(N-7):
    for j in range(M-7):
        
        for x in range(2):
            cnt = 0
            color = x

            for row in range(i,i+8):
                for col in range(j,j+8):
                    if(my_Map[row][col] != color_list[color%2]):
                        cnt += 1
                    color +=1
                color += 1


            min_count = min(min_count, cnt)

print(min_count)            
                