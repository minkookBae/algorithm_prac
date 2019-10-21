import sys
from copy import deepcopy

def mul_matrix(target_matrix1, target_matrix2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (target_matrix1[i][k] * target_matrix2[k][j])
            result[i][j] %= 1000
    
    return result

N, B = list(map(int,sys.stdin.readline().split()))
my_Matrix = []
for _ in range(N):
    my_Matrix.append(list(map(int,sys.stdin.readline().split())))

answer = [[0 for _ in range(N)] for _ in range(N)]
arr = deepcopy(my_Matrix)

for i in range(N):
    for j in range(N):
        if(i == j):
            answer[i][j] = 1

while(B > 0):
    if(B % 2 == 1):
        answer = mul_matrix(answer, arr)
    arr = mul_matrix(arr,arr)
    B = B // 2

for i in range(N):
    for j in range(N):
        print(answer[i][j],end=' ')
    print()