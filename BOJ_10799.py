import sys

target_str = sys.stdin.readline().rstrip()

stack = []
count = 0

for i in range(len(target_str)):
    if(target_str[i] == '('):
        stack.append(target_str[i])
    
    else:
        stack.pop()
        if(target_str[i-1] == '('):
            count += len(stack)
        else:
            count += 1

print(count)