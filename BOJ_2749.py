import sys

def fibo(N):

    a, b = 0, 1

    for i in range(N):
        a, b = b % (10**6), (a+b)%(10**6)
    
    return a

N = int(sys.stdin.readline())

print(fibo(N) % (10**6))

