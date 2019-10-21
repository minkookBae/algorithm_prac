import sys

def fact(n:int)->int:
    if(n == 0):
        return 1
    elif(n == 1 or n == 2):
        return n
    else:
        return fact(n-1) * n

N = int(sys.stdin.readline())

count = 0

for word in reversed(str(fact(N))):
    if(word == '0'):
        count += 1
    else:
        break
print(count)