import sys
sys.setrecursionlimit(10000)

line1 = input().split()
n = int(line1[0])

raw = input().strip().replace('{', '').replace('}', '')
parts = [p.strip() for p in raw.split(',') if p.strip()]

graph = [[] for _ in range(n)]
for i, p in enumerate(parts):
    graph[i].append(int(p))

used = [False] * n
found_cycle = False


def dfs(v, p):
    global found_cycle
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs(u, v)
        elif u != p:
            found_cycle = True


for i in range(n):
    if not used[i]:
        dfs(i, -1)

print('YES' if found_cycle else 'NO')
