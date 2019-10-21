import sys

A = []
B = []

N, M = list(map(int,sys.stdin.readline().split()))
for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

M, K = list(map(int,sys.stdin.readline().split()))
for _ in range(M):
    B.append(list(map(int,sys.stdin.readline().split())))

ret = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            ret[i][j] += A[i][k] * B[k][j]

for i in ret:
    for j in i:
        print(j,end=' ')
    print()