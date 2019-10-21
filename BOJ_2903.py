import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(15)]

# dp[0] = 2*2
# dp[1] = 3*3
# dp[2] = 5*5
# dp[3] = 9*9

cnt = 2
for i in range(15):
    cnt += cnt-1
    dp[i] = cnt**2

print(dp[N-1])