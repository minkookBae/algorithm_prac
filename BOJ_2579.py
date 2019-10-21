import sys

N = int(sys.stdin.readline())

step = [0]
visit = [0 for _ in range(N+1)]
for _ in range(N):
    step.append(int(sys.stdin.readline()))

i = 1
visit[1] = step[1]
visit[2] = visit[1] + step[2]

while(visit[N] == 0):
    visit[i] = max(visit[i-2] + step[i] , visit[i-3] + step[i-1] + step[i])
    i += 1

print(visit[N])