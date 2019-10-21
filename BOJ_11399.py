import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
ret = [0 for _ in range(N)]
P = sorted(P)
ret[0] = P[0]

for i in range(1,N):
    ret[i] = ret[i-1] + P[i]

print(sum(ret))