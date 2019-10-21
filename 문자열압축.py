from collections import deque
import sys

def solution(s):
    answer = 0
    length = len(s)
    if(length == 1):
        return 1
        
    min_num = sys.maxsize
    
    for cut in range(1, length//2 + 1):
        q = deque()    
        for i in range(0,length,cut):
            q.append(s[i:i+cut])
        
        for idx in range(len(q)-1):
            if(q[idx]):
                j = 0
                flag = True
                while(flag):
                    try:
                        if(q[idx] == q[idx+1+j]):
                            q[idx+1+j] = ""
                            j += 1
                        else:
                            flag = False
                    except IndexError:
                        break
                
                if(j>=1):
                    q[idx] = str(j+1) + q[idx]
        
        target_str = ""
        while(len(q) > 0):
            target_str += q.popleft()

        if(len(target_str) < min_num):
            min_num = len(target_str)

        answer = min_num                

    return answer


if __name__ == "__main__":
    s = "a"

    print(solution(s))