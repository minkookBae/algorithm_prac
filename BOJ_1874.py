import sys

N = int(sys.stdin.readline())

target_list = [0]

i = 1
j = 1
stack = []
visited = [0 for _ in range(0,N+2)]
result = []
count = 0
input_count = 0
while(count < 2*N):
    while(input_count < N):
        target_list.append(int(sys.stdin.readline()))
        input_count += 1
    if(target_list[i] not in stack):
        if(visited[j] == 0):
            stack.append(j)
            result.append("+")
        j+=1
        while(True):
            try:
                if(visited[j] == 1):
                    j+=1
                else:
                    break
            except IndexError:
                count = 2*N
                break

    elif(target_list[i] in stack):
        stack.pop()
        j -= 1
        while(True):
            if(visited[j] == 1):
                j-=1
            else:
                break
        visited[j] = 1
        i += 1
        result.append("-")
        if(i > N):
            break


if(visited.count(1) != N):
    print("NO")

else:
    for i in result:
        print(i)