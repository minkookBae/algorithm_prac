import sys
plastic_set = {}
for i in range(0,10):
    try:
        plastic_set[i] = 1
    except KeyError:
        plastic_set[i] = 1

N = str(int(sys.stdin.readline()))

count = 1

for alpha in N:

    if(plastic_set[int(alpha)] > 0):
        plastic_set[int(alpha)] -= 1

    else:

        if(int(alpha) == 6):
            if(plastic_set[9] > 0):
                plastic_set[9] -= 1
                continue
            else:
                for i in range(0,10):
                    plastic_set[i] += 1
                plastic_set[int(alpha)] -= 1
                count += 1

        elif(int(alpha) == 9):
            if(plastic_set[6] > 0):
                plastic_set[6] -= 1
            else:
                for i in range(0,10):
                    plastic_set[i] += 1
                plastic_set[int(alpha)] -= 1
                count += 1      

        else:
            for i in range(0,10):
                plastic_set[i] += 1
            plastic_set[int(alpha)] -= 1
            count += 1

print(count)