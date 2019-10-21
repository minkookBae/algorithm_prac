import sys

q = lambda : list(map(int,sys.stdin.readline().split()))

while(True):
    A, B = q()
    if(A == 0 and B == 0):
        break
    else:
        print(A+B)