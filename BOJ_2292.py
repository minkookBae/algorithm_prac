N = int(input())

i = 1
target_list = [1]
while(target_list[-1] < N):
    target_list.append(6*i + target_list[-1])
    i += 1

if(N == 1):
    print(1)
else:
    print(len(target_list))