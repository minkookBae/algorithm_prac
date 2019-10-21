import sys

N = int(sys.stdin.readline())
target_arr = []
target_str = "666"
i = 0
while(len(target_arr) < 10000):
    i += 1
    if target_str in str(i):
        target_arr.append(i)

print(target_arr[N-1])