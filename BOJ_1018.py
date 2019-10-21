import sys


q = lambda : list(map(int,sys.stdin.readline().split()))

N, M = q()

my_Map = [[] for _ in range(N)]
for i in range(N):
    temp = sys.stdin.readline().split()
    for alpha in temp[0]:
        my_Map[i].append(alpha)

min_num = 100000

for i in range(0,N-7):
    for j in range(0,M-7):
        color_list = ["B", "W"]
        

        for x in range(2):
            color = x
            cnt = 0

            for row in range(i,i+8):
                for col in range(j,j+8):
                    if(my_Map[row][col] != color_list[color%2]):
                        cnt += 1
                    color += 1
                color += 1
            
            if(min_num > cnt):
                min_num = cnt

    

print(min_num)
