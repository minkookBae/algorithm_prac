import sys

X = int(sys.stdin.readline())

target_list = []

for i in range(6,-1,-1):
    if(X == 2**i):
        target_list.append(2**i)
        break
    elif(2 ** (i-1) <= X < 2 ** i):
        target_list.append(2**(i-1))
        X -= 2**(i-1)

print(len(target_list))