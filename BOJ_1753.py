import sys
from collections import _heapq

input = sys.stdin.readline
INF = sys.maxsize

def solve(adj, K):
    prev = [-1] * (len(adj) + 1)
    dist = [INF] * (len(adj) + 1)
    dist[K] = 0

    priority_queue = []
    _heapq.heappush(priority_queue,[0, K])

    while priority_queue:
        current_dist , here = _heapq.heappop(priority_queue)

        for there, length in adj[here].items():
            next_dist = dist[here] + length

            if(next_dist < dist[there]):
                dist[there] = next_dist
                prev[there] = here
                _heapq.heappush(priority_queue, [next_dist, there])
    
    return dist, prev

if __name__ == "__main__":
    V, E = list(map(int,input().split()))
    K = int(input())

    adj = [{} for _ in range(V+1)]

    for _ in range(E):
        u, v, w = list(map(int,input().split()))

        if v in adj[u]:
            adj[u][v] = min(adj[u][v], w)
        else:
            adj[u][v] = w
    
    dist, prev = solve(adj,K)
    
    for d in dist[1:-1]:
        print(d if d != INF else "INF")