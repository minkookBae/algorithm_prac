from copy import deepcopy

def solve(w):
    if(w == ""):
        return ""
    
    u, v = "", ""
    stack = []
    count = 0
    for i in w:
        if(i == "(" or i == ")"):
            stack.append(i)
            count += 1
        if(stack.count('(') == stack.count(')')):
            break
    
    check = correct(stack)
    if(check):
        for i in stack:
            u += i
        v = w[count:]

    print(check, u,v)
    
def correct(stack:list)->bool:
    temp = deepcopy(stack)
    print(temp)
    stack2 = []
    while(len(temp) > 0):
        a = temp.pop()
        
        if(a == '('):
            stack2.append('(')
        elif(a == ")"):
            temp2 = stack2.pop()
            if(temp2 != "("):
                return False    

    return True


def solution(p):
   pass



if __name__ == "__main__":
    p = ")("	

    print(solve(p))