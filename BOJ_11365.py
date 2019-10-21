import sys

target_str = sys.stdin.readline()[:-1]

while(target_str != 'END'):
    print(target_str[::-1])
    target_str = sys.stdin.readline()[:-1]