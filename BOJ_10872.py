import sys

def fact(n):

    if(n == 0):
        return 1

    if(n == 1 or n == 2):
        return n

    return fact(n-1) * n

N = int(sys.stdin.readline())

print(fact(N))