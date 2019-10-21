import sys

N, K = list(map(int,sys.stdin.readline().split()))

people = [i for i in range(1,N+1)]

idx = 0
print("<",end='')
while(len(people) > 0):
    
    idx = (idx + K - 1)%len(people)
    poped_num = people.pop(idx)
    print(poped_num,end='')
    if(len(people) == 0):
        print(">")
    else:
        print(", ",end='')