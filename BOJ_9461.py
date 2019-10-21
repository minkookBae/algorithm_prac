import sys

T = int(sys.stdin.readline())

for _ in range(1,T+1):
    target_list = [1,1,1,2,2]
    N = int(sys.stdin.readline())
    
    if(N <= 5):
        print(target_list[N-1])
    else:
        for i in range(5,N):
           target_list.append(target_list[i-1]+target_list[i-5])
    
        print(target_list[N-1])