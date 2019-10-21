def solution(heights):
    answer = [0 for _ in range(len(heights))]

    for i in range(len(heights)-1,-1,-1):
        flag = False
        for j in range(i-1,-1,-1):
            if(heights[i] < heights[j]):
                flag = True
                answer[i] = j+1
                break
                
    
    return answer


if __name__ == "__main__":
    heights = [3,9,9,3,5,7,2]	

    print(solution(heights))