from collections import deque

def solution(prices):
    q = deque(prices)

    answer = [0 for _ in range(len(prices))]
    

    idx = 0
    while(q):
        target = q.popleft()
        for i in q:
            if(target <= i):
                answer[idx] += 1
            else:
                answer[idx] += 1
                break
        idx += 1

    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 8,12,52,22,7]
    print(solution(prices))