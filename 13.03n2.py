import heapq
import random
import time

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    total = 0
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            total += w
    return total

def prim(n, adj):
    in_mst = [False] * n
    total = 0
    pq = [(0, 0)]
    while pq:
        w, u = heapq.heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total += w
        for v, wt in adj[u]:
            if not in_mst[v]:
                heapq.heappush(pq, (wt, v))
    return total

def generate(n, m):
    edges = []
    used = set()
    for i in range(1, n):
        j = random.randint(0, i - 1)
        w = random.randint(1, 100)
        edges.append((w, i, j))
        used.add((min(i, j), max(i, j)))
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (min(u, v), max(u, v)) not in used:
            w = random.randint(1, 100)
            edges.append((w, u, v))
            used.add((min(u, v), max(u, v)))
    return edges

tests = [
    (10, 20), (50, 100), (100, 300), (200, 500), (300, 800),
    (400, 1000), (500, 1500), (600, 2000), (700, 2500), (800, 3000),
    (900, 3500), (1000, 4000), (1200, 5000), (1500, 6000), (2000, 8000)
]

print(f"{'N':>6} {'M':>6} {'Prim(s)':>10} {'Kruskal(s)':>12}")
print("-" * 40)

for n, m in tests:
    edges = generate(n, m)
    adj = [[] for _ in range(n)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    t0 = time.perf_counter()
    prim(n, adj)
    t_prim = time.perf_counter() - t0

    t0 = time.perf_counter()
    kruskal(n, edges)
    t_kruskal = time.perf_counter() - t0

    print(f"{n:>6} {m:>6} {t_prim:>10.6f} {t_kruskal:>12.6f}")

print()
print("Алгоритмическая сложность:")
print("Прим:    O(E log V) — heapq + список смежности")
print("Краскал: O(E log E) — сортировка рёбер + DSU")
print("На разреженных графах оба схожи.")
print("На плотных графах Краскал быстрее из-за меньшей константы.")
