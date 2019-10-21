import sys

target_list = sys.stdin.readline().split('-')

for i in target_list:
    print(i[0],end='')
