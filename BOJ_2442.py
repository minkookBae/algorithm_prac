import sys

input = sys.stdin.readline
N = int(input().rstrip())

for i in range(1,N+1):
    print(" " * (N-i),end='')
    print("*" * (2*i - 1),end=' ')
    print()