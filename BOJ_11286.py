import sys
from collections import _heapq

heap = []
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())

    if( num == 0 ):
        if(len(heap) > 0):
            result = _heapq.heappop(heap)
            print(result[0] * result[1])
        else:
            print(0)
    
    else:
        _heapq.heappush(heap, (abs(num), 1 if num > 0 else -1))
    