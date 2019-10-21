import sys

A = int(sys.stdin.readline()) % (10**9+7)
X = int(sys.stdin.readline())

i = 1
mod_list = [1,A]
while(i <= X):
    mod_list.append((mod_list[-1]**2)%(10**9+7))
    i *= 2

temp = bin(X)[2:]

count = 1
idx = 1
for i in reversed(temp):
    if(i == "1"):
        count *= mod_list[idx]
    idx += 1

print(count % (10**9+ 7))