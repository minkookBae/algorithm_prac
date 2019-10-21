import sys

N = int(sys.stdin.readline())
target_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

low = 0
high = max(target_list)
m = 0

while(low <= high):
    mid = (low + high + 1) // 2

    count = 0
    
    for i in target_list:
        if(i > mid):
            count += mid
        else:
            count += i
    if( count <= M ):
        low = mid + 1
        if(mid > m):
            m = mid
    
    else:
        high = mid -1

print(m)