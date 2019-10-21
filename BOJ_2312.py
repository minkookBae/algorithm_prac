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
    N = int(sys.stdin.readline())
    primelist = prime_list(N+1)

    prime_dict = {}


    while(N != 1):
        
        for i in primelist:
            if(N % i == 0):
                try:
                    prime_dict[i] += 1
                except KeyError:
                    prime_dict[i] = 1
                
                N = int(N/i)

    for k,v in prime_dict.items():
        print(k, v)