import sys

q = lambda : list(map(int,sys.stdin.readline().split()))

E, S, M = q()

A, B, C = 1, 1, 1
count = 1

while(True):
    if(E == 1 and S == 1 and M == 1):
        break
    A += 1
    B += 1
    C += 1
    count += 1

    if(A == 16):
        A = 1
    if(B == 29):
        B = 1
    if(C == 20):
        C = 1
    
    if(A == E and B == S and C == M):
        break
print(count)