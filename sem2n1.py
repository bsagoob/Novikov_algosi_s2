import heapq

line1 = input().split()
n, m, s, f = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3])

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [float('inf')] * n
prev = [-1] * n
dist[s] = 0
pq = [(0, s)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))

path = []
cur = f
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(len(path))
