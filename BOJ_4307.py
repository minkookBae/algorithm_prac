import sys

T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    poll_len, n = list(map(int,sys.stdin.readline().split()))

    ant_list = []
    for _ in range(n):
        ant_list.append(int(sys.stdin.readline()))

    min_ant = 2**31
    max_ant = -1 * (2**31)
    max_value , min_value = 0, 0
    for i in range(n):
        max_ant = max(ant_list[i], poll_len - ant_list[i])
        min_ant = min(ant_list[i], poll_len - ant_list[i])
        
        max_value = max(max_ant, max_value)
        min_value = max(min_ant, min_value)

    
    print(min_value, max_value)