import sys

def solve(my_Map, i, j):
    global count

    my_Map[i][j] = count
    my_Map[i][j+1] = count + 1
    my_Map[i+1][j] = count + 2
    my_Map[i+1][j+1] = count + 3
    count += 4

N, r, c = list(map(int,sys.stdin.readline().split()))

size = 2 ** N
my_Map = [[0 for _ in range(size)] for _ in range(size)]
count = 0

for i in range(0,size,2):
    for j in range(0,size,2):
        solve(my_Map,i,j)

for i in range(size):
    for j in range(size):
        print(my_Map[i][j],end=' ')
    print()