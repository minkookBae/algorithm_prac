import sys

N, M = list(map(int,sys.stdin.readline().split()))

target_list = list(map(int,sys.stdin.readline().split()))

low = 0
m = 0
high = max(target_list)

while(low <= high):
    mid = (low + high + 1) // 2
    count = 0

    for i in target_list:
        if(i > mid):
            count += i - mid
    
    if(count >= M):
        low = mid + 1
        if(m < mid):
            m = mid
    else:
        high = mid -1
    
print(m)