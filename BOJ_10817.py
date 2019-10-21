import sys

q = lambda : list(map(int,sys.stdin.readline().split()))

A = q()

max_num = max(A)
idx = A.index(max_num)
A.pop(idx)
print(max(A))