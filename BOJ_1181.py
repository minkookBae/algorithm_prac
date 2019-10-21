import sys

N = int(sys.stdin.readline())

target_list = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    target_list.append(temp)
    
target_list = list(set(target_list))

result_list = [[i] for i in range(51)]

for word in sorted(target_list):
    result_list[len(word)].append(word)

for sub_list in result_list:
    if(len(sub_list) > 1) : 
        for j in range(1,len(sub_list)):
            print(sub_list[j])
