# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    answer = []
    no_1 = [0 for _ in range(len(answers)+1)]
    no_2 = [0 for _ in range(len(answers)+1)]
    no_3 = [0 for _ in range(len(answers)+1)]

    for i in range(1,len(answers)+1):
        no_1[i] = i%5
        if(no_1[i] == 0):
            no_1[i] = 5
    
    temp = 1
    for i in range(1,len(answers)+1):
        if(i%2 != 0): # odd num
            no_2[i] = 2
        else :  # even num
            no_2[i] = temp
            temp += 1
            if(temp == 2):
                temp += 1
            if(temp == 6):
                temp = 1

    for i in range(1,len(answers)+1):
        if(i%10 == 1 or i%10 == 2):
            no_3[i] = 3
        elif(i%10 == 3 or i%10 == 4):
            no_3[i] = 1
        elif(i%10 == 5 or i%10 == 6):
            no_3[i] = 2
        elif(i%10 == 7 or i%10 == 8):
            no_3[i] = 4
        elif(i%10 == 9 or i%10 == 0):
            no_3[i] = 5

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i in range(len(answers)):
        if(no_1[i+1] == answers[i]):
            count_1 += 1

        if(no_2[i+1] == answers[i]):
            count_2 += 1

        if(no_3[i+1] == answers[i]):
            count_3 += 1
    
    target_list = [0,count_1,count_2,count_3]
    max_num = max(target_list)

    for i in range(len(target_list)):
        if(max_num == target_list[i]):
            answer.append(i)

    return answer
