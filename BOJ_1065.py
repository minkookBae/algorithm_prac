import sys

N = int(sys.stdin.readline())

count = 99
if(N < 100):
    print(N)
elif(N == 1000):
    print(144)
else:
    for i in range(100,N+1):
        temp = str(i)
        if(int(temp[0]) - int(temp[1]) == int(temp[1]) - int(temp[2])):
            count +=1

    print(count)