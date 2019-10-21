import sys

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    
    return a

N = int(sys.stdin.readline())

print(fibo(N))