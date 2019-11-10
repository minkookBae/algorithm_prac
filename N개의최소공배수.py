from math import gcd

def solution(arr):
    answer = 0

    while(len(arr) != 1):
        a = arr.pop()
        b = arr.pop()
        c = gcd(a,b)
        print(a,b,c)
        arr.insert(0,int(a*b/c))
    
    answer = arr[0]
    return answer