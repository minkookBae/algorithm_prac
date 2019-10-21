import sys
from copy import deepcopy

A, B = list(map(int,sys.stdin.readline().split()))

gcd = deepcopy(A)
gcd2 = deepcopy(B)

while gcd2:
    gcd, gcd2 = gcd2, gcd%gcd2

print(gcd)
print((A*B)//gcd)
