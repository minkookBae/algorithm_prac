import sys
from itertools import permutations

q = lambda : list(map(int,sys.stdin.readline().split()))
N = int(sys.stdin.readline())
target_list = q()
operator = q()
operator_list = []
for i,count in enumerate(operator):
    for _ in range(count):
        if(i == 0):
            operator_list.append('+')
        elif(i == 1):
            operator_list.append('-')
        elif(i == 2):
            operator_list.append('*')
        elif(i == 3):
            operator_list.append('/')

permu_list = permutations(operator_list,N-1)
max_num = (-1) * (sys.maxsize - 1)
min_num = sys.maxsize

for case in permu_list:
    temp = target_list[0]
    for i in range(len(case)):
        if(case[i] == '+'):
            temp += target_list[i+1]
        elif(case[i] == '-'):
            temp -= target_list[i+1]
        elif(case[i] == '*'):
            temp *= target_list[i+1]
        elif(case[i] == '/'):
            if(temp < 0):
                temp = (-1) * temp
                temp = temp // target_list[i+1]
                temp = (-1) * temp
            else:
                temp = temp // target_list[i+1]
    
    if(max_num < temp):
        max_num = temp
    
    if(min_num > temp):
        min_num = temp

print(max_num)
print(min_num)