import sys

N = int(sys.stdin.readline())
my_Map = []

for _ in range(N):
    a, b, c = list(map(int,sys.stdin.readline().split()))
    my_Map.append([a,b,c])

dp = [[0,0,0] for _ in range(N)]
dp[0][0] = my_Map[0][0]
dp[0][1] = my_Map[0][1]
dp[0][2] = my_Map[0][2]


for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + my_Map[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + my_Map[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + my_Map[i][2]

print(min(dp[N-1]))