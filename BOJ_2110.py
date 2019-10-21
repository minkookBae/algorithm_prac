import sys

def routerInstall(distance):
    count = 1
    cur_home = target_list[0]
    for i in range(1,N):
        if (distance <= target_list[i] - cur_home):
            count += 1
            cur_home = target_list[i]
    
    return count


N, C = list(map(int,sys.stdin.readline().split()))
target_list = []

for _ in range(N):
    target_list.append(int(sys.stdin.readline()))

target_list.sort()

low = 1
high = target_list[-1] - target_list[0]

while(low <= high):
    mid = (low + high + 1) // 2

    router_count = routerInstall(mid)

    if(router_count < C):
        high = mid -1
    
    else:
        answer = mid
        low = mid + 1

print(answer)