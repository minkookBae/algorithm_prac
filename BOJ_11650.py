import sys

N = int(sys.stdin.readline())

target_list = []
for _ in range(N):
    x, y = list(map(int,sys.stdin.readline().split()))
    target_list.append([x,y])

for i in sorted(target_list):
    print("{} {}".format(i[0],i[1]))