import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, t = map(int, input().split())
        edges.append((x, y, t))

    dist = [float('inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        for x, y, t in edges:
            if dist[x] != float('inf') and dist[x] + t < dist[y]:
                dist[y] = dist[x] + t

    has_negative_cycle = False
    for x, y, t in edges:
        if dist[x] != float('inf') and dist[x] + t < dist[y]:
            has_negative_cycle = True
            break

    print("возможно" if has_negative_cycle else "не возможно")
