import sys

input = sys.stdin.readline
N = int(input().rstrip())

print(" " * (N-1),end='')
print("*")
for i in range(1,N):
    print(" " * (N-i) ,end='')
    print("*",end='')
    print(" " * (i),end='')
    print(" " * (i-1),end='')
    print("*")