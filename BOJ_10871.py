import sys

q = lambda : list(map(int,sys.stdin.readline().split()))

N, X = q()

A = q()

for i in A:
    if i < X:
        print(i,end=' ')