import sys

n, k = list(map(int,sys.stdin.readline().split()))

coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [10001 for _ in range(100000)]
for i in coin:
    dp[i] = 1
for i in range(len(coin)):
    for j in range(1,k+1):
        if(j - coin[i] > 0):
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

if(dp[k] != 10001):
    print(dp[k])
else:
    print(-1)