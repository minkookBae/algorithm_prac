import sys
from collections import deque

def D(q):
    if q:
        q.popleft()
        return q
    else:
        return "error"

def D2(q):
    if q:
        q.pop()
        return q
    else:
        return "error"

T = int(sys.stdin.readline())

for _ in range(1,T+1):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())

    reverse_count = 0

    target_list = deque(eval(sys.stdin.readline()))
    flag = True

    for word in p:
        if(word == 'R'):    
            reverse_count += 1
        
        elif(word == 'D'):
            if(reverse_count % 2 == 0):
                target_list = D(target_list)
                if(target_list =="error"):
                    flag = False
                    break
            
            else:
                target_list = D2(target_list)
                if(target_list == "error"):
                    flag = False
                    break
                
    
    if(flag):
        print("[",end='')
        if target_list:
            if(reverse_count%2 == 0):
                
                    for i in range(0,len(target_list)-1):
                        print("{},".format(target_list[i]),end='')
                    print("{}]".format(target_list[len(target_list)-1]))
                
            else:
                
                    for i in range(len(target_list)-1,0,-1):
                        print("{},".format(target_list[i]),end='')
                    print("{}]".format(target_list[0]))
        else:
            print("]")            
    else:
        print("error")