import sys

K, N = list(map(int,sys.stdin.readline().split()))
target_list = []
for _ in range(K):
    target_list.append(int(sys.stdin.readline()))

low = 0
m = 0
high = max(target_list)

while (low <= high):
    mid = (low + high +1 ) // 2 # 이진 mid 계산
    count = 0

    for i in target_list:
        count += (i // mid) # 랜선 갯수 count

    if (count >= N): # 너무 많이 잘리면
        low = mid + 1 # low를 mid로
        if(mid > m):
            m = mid
    
    else:
        high = mid - 1 # 너무 적게 잘리면 high를 mid로

print(m)