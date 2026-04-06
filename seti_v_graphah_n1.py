from collections import deque

def bfs(graph, source, sink, parent, n):
    visited = [False] * (n + 1)
    visited[source] = True
    q = deque([source])
    while q:
        u = q.popleft()
        for v in range(1, n + 1):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
                q.append(v)
    return False

def max_flow(n, s, t, graph):
    parent = [-1] * (n + 1)
    flow = 0
    while bfs(graph, s, t, parent, n):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        flow += path_flow
        parent = [-1] * (n + 1)
    return flow

import sys
input_data = sys.stdin.read().split('\n')
idx = 0
net = 1

while idx < len(input_data):
    line = input_data[idx].strip()
    idx += 1
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    s, t, c = map(int, input_data[idx].split())
    idx += 1
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(c):
        u, v, w = map(int, input_data[idx].split())
        idx += 1
        graph[u][v] += w
        graph[v][u] += w
    print(f"Network {net}")
    print(f"The bandwidth is {max_flow(n, s, t, graph)}.")
    net += 1
