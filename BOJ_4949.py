import sys

def VPS(string):
    stack = []
    flag = True
    for word in string:
        if(word =='('):
            stack.append(word)
        
        elif(word =='['):
            stack.append(word)
        
        elif(word ==')'):
            if(len(stack) > 0):
                temp = stack.pop()
                if(temp != '('):
                    flag = False
                    break
            else:
                flag = False
                break
        elif(word==']'):
            if(len(stack) > 0):
                temp = stack.pop()
                if(temp != '['):
                    flag = False
                    break
            else:
                flag = False
                break
    if(len(stack) == 0):
        return flag
    else:
        return False

flag = True

while(flag):
    target_str = sys.stdin.readline().rstrip()
    if(target_str == "."):
        flag = False
        continue
    
    if(VPS(target_str)):
        print("yes")
    else:
        print("no")