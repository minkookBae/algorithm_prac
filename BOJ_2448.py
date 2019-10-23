import sys

input = sys.stdin.readline
N = int(input().rstrip())
myMap = [[' ' for _ in range(2 * N)] for _ in range(N)]

def solve(n:int, x, y):
    if(n == 3):
        myMap[y][x] = "*"
        myMap[y+1][x-1] = "*"
        myMap[y+1][x+1] = "*"
        myMap[y+2][x-2] = "*"
        myMap[y+2][x-1] = "*"
        myMap[y+2][x] = "*"
        myMap[y+2][x+1] = "*"
        myMap[y+2][x+2] = "*"
        return
    
    div = n // 2
    solve(div, x, y)
    solve(div, x - div, y + div)
    solve(div, x + div, y + div)



solve(N, N-1, 0)

for i in range(N):
    print("".join(myMap[i]))