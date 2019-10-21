number = {"0001101" : 0, "0011001" : 1, "0010011" : 2, "0111101" : 3, "0100011" : 4, "0110001" : 5, "0101111" : 6, "0111011" : 7, "0110111" : 8, "0001011" : 9}

def validate(arr):
    odd = arr[0] + arr[2] + arr[4] + arr[6]
    even = arr[1] + arr[3] + arr[5]
    final_num = odd * 3 + even + arr[7]

    if(final_num % 10 == 0):
        return True
    else:
        return False

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[] for i in range(N)]
    for i in range(N):
        arr[i].append(input())

    flag = False
    temp_str = ''
    for i in range(N):
        if(flag):
            break
        for j in range(M-1,-1,-1):
            if(flag):
                break
            if(arr[i][0][j] == '1'):

                temp_str = arr[i][0][j-55:j+1]
                flag = True

    # 암호 따내기

    password = []
    for i in range(0,56,7):
        password.append(temp_str[i:i+7])

    password2 = []
    for i in password:
        if(i in number):
            password2.append(number[i])
    
    if(validate(password2)):
        print("#{} {}".format(test_case, sum(password2)))
    else:
        print("#{} {}".format(test_case, 0))