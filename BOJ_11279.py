import sys
from collections import _heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if(num != 0):
        _heapq.heappush(heap,(-num,num))
    else: # num == 0
        if(len(heap) == 0):
            print(0)
        else:
            print(_heapq.heappop(heap)[1])
