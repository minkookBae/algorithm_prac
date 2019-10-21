import sys

def VPS(string):
    stack = []
    for word in string:
        if(word == '('):
            stack.append(word)
        elif(word == ')'):
            if(len(stack) > 0):
                temp = stack.pop(-1)
                if(temp != '('):
                    return 'NO'
            else:
                return 'NO'
    
    if(len(stack) == 0):
        return 'YES'
    else:
        return 'NO'


q = lambda : sys.stdin.readline().rstrip()
q2 = lambda : int(sys.stdin.readline())

T = q2()

for _ in range(T):
    target_str = q()
    print(VPS(target_str))