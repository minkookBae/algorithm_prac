import sys

def solve(N):
    a, b = 1, 3
    
    for _ in range(N):
        a, b = b, 2*a + b

    return a

N = int(sys.stdin.readline())

print(solve(N-1)%10007)