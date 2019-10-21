import sys
from math import gcd

A, B = list(map(int,sys.stdin.readline().split()))

print(gcd(A,B) * '1')