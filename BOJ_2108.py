import sys
from collections import Counter

N = int(sys.stdin.readline())

target_list = []
for _ in range(N):
    target_list.append(int(sys.stdin.readline()))

sum = 0
for i in target_list:
    sum += i
print(int(round(sum/N,0)))
print(sorted(target_list)[N//2])

counter_dict = Counter(target_list)
result_list = []
for k,v in counter_dict.items():
    if(v == max(counter_dict.values())):
        result_list.append(k)
if(len(result_list) > 1):
    print(sorted(result_list)[1])
else:
    print(result_list[0])

print(max(target_list) - min(target_list))