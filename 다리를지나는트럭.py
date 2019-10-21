from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    complete_cross = deque()
    crossing_bridge = deque()

    time = 0
    while(len(complete_cross) != len(truck_weights)):

        for i in crossing_bridge:
            i[1] -= 1

        temp_list = []

        for i in range(len(crossing_bridge)):
            if(crossing_bridge[i][1] == 0):
                complete_cross.append(crossing_bridge[i][0])
                temp_list.append(i)
        
        for i in range(len(temp_list)):
            crossing_bridge.popleft()


        temp_sum = 0
        for i in crossing_bridge:
            temp_sum += i[0]
        if(truck_queue):
            temp_sum += truck_queue[0]
            if(temp_sum <= weight):
                temp = truck_queue.popleft()
                crossing_bridge.append([temp,bridge_length])


        time += 1

    answer = time

    return answer



if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]	

    print(solution(bridge_length,weight,truck_weights))