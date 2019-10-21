import sys
x, y, w, h = list(map(int,sys.stdin.readline().split()))

target_list = []

target_list.append(x)
target_list.append(y)
target_list.append(w-x)
target_list.append(h-y)


print(min(target_list))