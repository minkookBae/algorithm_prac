import sys
from collections import deque

def solve(n):
    a, b = 1, 2

    for i in range(n):
        a, b = b , a + b

    return a

N = int(sys.stdin.readline())

print(solve(N-1)%10007)