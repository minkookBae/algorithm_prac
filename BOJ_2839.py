import sys

N = int(sys.stdin.readline())
count = 0
if(N == 4 or N == 7):
    print(-1)

else:
    while(N % 5 != 0):
        N -= 3
        count += 1
    count += N // 5

    print(count)