import sys

N = int(sys.stdin.readline())

dp = [0,0,1,1] # 0번째는 없애고, 1,2,3을 각각 0회, 1회, 1회로 초기화

for i in range(4,N+1):
    dp.append(dp[i-1] + 1) # 1을 뺄 떄의 경우

    if(i%3 == 0):
        dp[i] = min(dp[i], dp[i//3]+1)
    
    elif(i%2 == 0):
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])