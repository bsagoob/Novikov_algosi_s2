from collections import deque

line1 = input().split()
n, m = int(line1[0]), int(line1[1])

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * n
dist[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    for u in graph[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)

for d in dist:
    print(d)
