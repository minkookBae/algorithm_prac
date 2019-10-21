import sys

N = int(sys.stdin.readline())

target_list = [0 for _ in range(10001)]

for _ in range(N):
    temp = int(sys.stdin.readline())
    target_list[temp] += 1

for i in range(len(target_list)):
    if(target_list[i] > 0):
        for _ in range(target_list[i]):
            print(i)