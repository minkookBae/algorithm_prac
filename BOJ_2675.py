import sys

T = int(sys.stdin.readline()[:-1])

for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    for i in S:
        print(i * R,end='')
    print()
