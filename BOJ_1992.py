import sys

def solve(x, y, length):
    
    compare = my_Map[x][y]
    is_same = True

    for i in range(x,x+length):
        for j in range(y,y+length):
            if(my_Map[i][j] != compare):
                is_same = False
                break                
    
    if(is_same):
        print(compare,end='')
    else:
        print("(",end='')
        solve(x, y, length // 2) # 2사분면
        solve(x, y+length//2 , length//2) # 1사분면
        solve(x+length//2 , y , length // 2) # 3사분면
        solve(x+length//2, y+length//2 , length//2) # 4사분면
        print(")",end='')

    
N = int(sys.stdin.readline())
my_Map = [[] for _ in range(N)]
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    for word in temp:
        my_Map[i].append(word)

solve(0,0,N)

