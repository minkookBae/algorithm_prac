import sys

T = int(input())

q = lambda : list(map(int,sys.stdin.readline().split()))

for _ in range(T):
    A, B = q()
    print(A+B)