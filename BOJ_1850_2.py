import sys

A, B = list(map(int,sys.stdin.readline().split()))

while B:
    A, B = B, A%B

print(A * '1')