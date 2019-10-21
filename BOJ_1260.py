import sys
from collections import deque

def dfs(v):
    visit_dfs[v] = 1
    print(v,end=' ')
    for i in range(1,N+1):
        next = i
        if(visit_dfs[next] == 0 and my_Map[v][next] == 1):
            dfs(next)

def bfs(v):
    q.append(v)
    visit_bfs[v] = 1
    
    while(len(q) != 0):
        current = q.popleft()
        print(current,end=' ')
        for i in range(1,N+1):
            if(visit_bfs[i] == 0 and my_Map[current][i] == 1):
                visit_bfs[i] = 1
                q.append(i)


N, M, V = list(map(int,sys.stdin.readline().split()))

my_Map = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit_dfs = [0 for _ in range(N+1)]
visit_bfs = [0 for _ in range(N+1)]
q = deque()
    
for _ in range(M):
    i, j = list(map(int,sys.stdin.readline().split()))
    my_Map[i][j] = 1
    my_Map[j][i] = 1

dfs(V)
print()
bfs(V)