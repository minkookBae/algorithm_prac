import sys

def avg(N,target_list):
    temp = sum(target_list)
    avg_list = temp / N
    return avg_list

q = lambda : list(map(int,sys.stdin.readline().split()))

C = int(sys.stdin.readline())

for i in range(C):
    
    count = 0
    target_list = q()
    N = target_list[0]
    target_list = target_list[1:]

    temp_avg = avg(N,target_list)
    for j in target_list:
        if j > temp_avg:
            count += 1


    answer = count / N * 100

    print("%.3f"%answer,end="%")
    print()