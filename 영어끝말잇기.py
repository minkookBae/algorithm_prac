def solution(n, words):
    answer = [0,0]
    word_dict = {}
    flag = True
    idx = 0
    for i in range(len(words)-1):
        if not flag:
            break
        
        if(words[i][-1] != words[i+1][0]):
            flag = False
            idx = i
        
        if(words[i] not in word_dict):
            word_dict[words[i]] = 1
        
        else:
            flag = False
            idx = i
            break
    
    
    print(idx)

    if(flag):
        return [0,0]
    
    else:

        return answer