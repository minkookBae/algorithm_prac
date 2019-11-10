def solution(A,B):
    answer = 0
    A.sort()
    B.sort()

    temp_sum = 0
    for i in range(len(A)):
        temp_sum += A[i] * B[len(B) -1 - i]

    answer = temp_sum

    return answer