import sys

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    temp = prime_list(n)
    
    for i in range(n//2,1,-1):
        if(i in temp and n-i in temp):
            print(i,n-i)
            break