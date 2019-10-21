import sys

def push(x):
    target_list.append(x)

def pop():
    target_list.pop(-1)

q = lambda : int(sys.stdin.readline())
K = q()
target_list = []
    
for _ in range(K):
    N = q()
    
    if(N == 0):
        pop()
    else:
        push(N)

print(sum(target_list))