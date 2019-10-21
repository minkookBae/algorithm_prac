import sys

def prime_list(start,n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(start, n) if sieve[i] == True]

flag = True
while(flag):
    n = int(sys.stdin.readline())
    if(n == 0):
        flag = False
        continue
    print(len(prime_list(n+1,2*n+1)))
