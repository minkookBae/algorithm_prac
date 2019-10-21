import sys
from collections import _heapq

def middle_heapq(heap,middle):
    temp_heap = []
    for num in heap:
        _heapq.heappush(temp_heap,num)
    
    middle_num = 0
    for _ in range(middle):
        middle_num = _heapq.heappop(temp_heap)
    
    return middle_num

heap = []
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())
    _heapq.heappush(heap,num)
    if(len(heap) % 2 == 0):
        print(middle_heapq(heap,len(heap)//2))
    else:
        print(middle_heapq(heap,len(heap)//2+1))