def solution(progresses, speeds):
    
    answer = []

    i = 0
    count = [0 for _ in range(len(progresses))]
    while(i<len(progresses)):
        progresses[i] += speeds[i]
        count[i] += 1
        if(progresses[i] >= 100) :
            i += 1
    
    max_num = count[0]
    result = [1]
    j = 0
    for i in range(1,len(progresses)):
        if(max_num < count[i]):
            max_num = count[i]
            result.append(1)
            j += 1
        else:
            result[j] += 1


    return result


if __name__ == "__main__":
    a = [93,30,55]
    b = [1,30,5]

    print(solution(a,b))