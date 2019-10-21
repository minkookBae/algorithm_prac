import sys

T = int(sys.stdin.readline())

for test_case in range(1,T+1):

    N = int(sys.stdin.readline())
    
    worker = []
    for i in range(N):
        paper, interview = list(map(int,sys.stdin.readline().split()))
        worker.append([paper,interview])
    
    worker = sorted(worker, key = lambda x : x[0])
    
    pivot = worker[0]
    count = 1

    for i in range(1,len(worker)):
        if(worker[i][1] < pivot[1]): # 합격
            count += 1
            pivot = worker[i]

    print(count)