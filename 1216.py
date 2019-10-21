from copy import deepcopy

def palindrome(target):
    flag = True
    for i in range(len(target)//2):
        if(target[i] != target[len(target)-1-i]):
            flag = False

    return flag

for test_case in range(1,11):
    T = int(input())
    arr = [[] for i in range(100)]
    count = 0

    for i in range(100):
        temp = input()
        for j in range(100):
            arr[i].append(temp[j])
    # 입력받기

    length = 1
    max_count = 0
    flag = True
    while(flag):
        for i in range(100):
            for j in range(101-length):
                target_str = ''
                for k in range(length):
                    target_str += arr[i][j+k-1]
            
                if (palindrome(target_str)):
                    max_count = deepcopy(length)
                    length += 1
                else:
                    flag = False

    # 가로 계산

    flag = True
    length = 1
    max_count2 = 0
    while(flag):
        for i in range(100):
            for j in range(101-length):
                target_str = ''
                for k in range(length):
                    target_str += arr[j+k-1][i]
            
                if (palindrome(target_str)):
                    max_count2 = deepcopy(length)
                    length += 1
                else:
                    flag = False

    # 세로 계산
    
    print("#{} {}".format(test_case, max(max_count,max_count2)))