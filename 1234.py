from copy import deepcopy

for test_case in range(1,11):
    N, M = map(int,input().split())

    temp_arr = deepcopy(M)
    temp_arr = str(temp_arr)
    
    flag = True
    while(flag):
        length = len(temp_arr)
        i = 0
        while(True):
            temp_str = ''
            if(temp_arr[i] == temp_arr[i+1]):
                temp_str += temp_arr[0:i]
                temp_str += temp_arr[i+2:]
                temp_arr = deepcopy(temp_str)
                break
            elif(i == length-2 and temp_arr[i] != temp_arr[i+1]):
                flag = False
                break
            
            i += 1

    print("#{} {}".format(test_case,int(temp_arr)))