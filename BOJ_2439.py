N = int(input())

for i in range(1,N+1):
    temp = N-i
    print(' ' * temp ,end='')
    print('*' * i)