import sys
from copy import deepcopy

A, B = list(map(int,sys.stdin.readline().split(":")))

C = deepcopy(A)
D = deepcopy(B)

while D:
    C, D = D, C % D

print("{}:{}".format(A//C,B//C))