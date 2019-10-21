import sys

def hanoi(disk, start, mid, end):
    if(disk == 1):
        print(start, end)
    else:
        hanoi(disk-1, start, end, mid)
        print(start,end)
        hanoi(disk-1, mid, start, end)

N = int(sys.stdin.readline())
K = 0

for disk in range(N):
    K *= 2
    K += 1

print(K)
hanoi(N,1,2,3)