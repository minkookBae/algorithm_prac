import sys

T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    n = int(sys.stdin.readline())
    row1 = list(map(int,sys.stdin.readline().split()))
    row2 = list(map(int,sys.stdin.readline().split()))
    sticker = []
    row1.insert(0,0)
    row2.insert(0,0)
    sticker.append(row1)
    sticker.append(row2)

    dp = [[0,0,0] for _ in range(n+1)]
    dp[1][0] = sticker[0][1]
    dp[1][1] = sticker[1][1]

    for i in range(2,n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + sticker[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + sticker[1][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

    print(max(dp[n]))
