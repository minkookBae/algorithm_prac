import sys

input = sys.stdin.readline
N = int(input().rstrip())

for i in range(1,N):
    print("*" * i,end='')
    print(" " * (N-i) * 2,end='')
    print("*" * i,end='')
    print()
    

for i in range(N,0,-1):
    print("*" * i,end='')
    print(" " * (N-i) * 2,end='')
    print("*" * i,end='')
    print()
    