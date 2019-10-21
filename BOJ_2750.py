import sys
N = int(sys.stdin.readline())

target_array = []
for _ in range(N):
    target_array.append(int(sys.stdin.readline()))

target_array.sort()

for i in target_array:
    print(i)