import heapq
from math import sqrt

n = int(input())
coords = []
for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

def dist(a, b):
    return sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

d = [float('inf')] * n
d[0] = 0
pq = [(0, 0)]

while pq:
    cost, u = heapq.heappop(pq)
    if cost > d[u]:
        continue
    for v in range(n):
        if v != u:
            new_cost = max(cost, dist(u, v))
            if new_cost < d[v]:
                d[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

print(f"{d[1]:.3f}")
