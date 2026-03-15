import heapq
import sys
input = sys.stdin.readline

line = input().split()
n, m = int(line[0]), int(line[1])
centers = list(map(int, line[2:]))

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [float('inf')] * n
pq = []
for c in centers:
    dist[c] = 0
    heapq.heappush(pq, (0, c))

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

total = 0
for i in range(n):
    if i not in centers and dist[i] != float('inf'):
        total += dist[i]

print(total)
