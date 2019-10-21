import sys

n, k = list(map(int,sys.stdin.readline().split()))

coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(len(coin)):
    for j in range(1,k+1):
        if(j-coin[i] >= 0):
            dp[j] += dp[j- coin[i]]
    
print(dp[k])