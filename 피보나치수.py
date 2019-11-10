def fibo(n):
    a, b = 0 , 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567

def solution(n):
    answer = fibo(n)
    return answer