import sys
from collections import Counter

N = int(sys.stdin.readline())
A = map(int,sys.stdin.readline().split())

c = Counter(A)

M = int(sys.stdin.readline())
B = map(int,sys.stdin.readline().split())


for i in B:
    if i in c:
        print(1)
    else:
        print(0)
    