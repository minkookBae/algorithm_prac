import sys

N, K = list(map(int,sys.stdin.readline().split()))

coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))

count = 0
while (K != 0):
    for i in range(N-1,-1,-1):
        if(K >= coin[i]):
            temp = K // coin[i]
            count += temp
            K -= temp * coin[i]
            break

print(count)