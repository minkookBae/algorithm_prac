from collections import deque

def solution(priorities, location):

    q = deque(priorities)
    location_queue = deque()
    for i in range(len(priorities)):
        location_queue.append(0)
    location_queue[location] = 1

    count = 0

    while(len(q) > 0 and len(location_queue) > 0):
        temp = q.popleft()

        if(len(q) == 0):
            answer = count + 1
            break

        if(temp < max(q)):
            q.append(temp)
            location_queue.append(location_queue.popleft())
        
        else:
            temp_location = location_queue.popleft()
            count += 1
            if(temp_location == 1):
                answer = count
                break
    
    return answer



if __name__ == "__main__":
    priorities = [2]
    location = 0

    print(solution(priorities, location))