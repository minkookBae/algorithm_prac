import sys
from collections import deque

def solve(N):
    if(len(q) == N):
        return q[N]
    
    else:
        q[N] = solve(N // P) + solve(N // Q)
        return 

N, P, Q = list(map(int,sys.stdin.readline().split()))

q = deque([1])

print(solve(N))