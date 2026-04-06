from collections import deque, defaultdict

def bfs_dist(start, adj, max_node):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

t = int(input())
for _ in range(t):
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    e = int(input())
    adj = defaultdict(list)
    for _ in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    try:
        input()
    except:
        pass

    from collections import Counter
    have = Counter(cards)
    need = Counter(range(1, n + 1))

    total = 0
    for card in range(1, n + 1):
        extra = have[card] - need[card]
        if extra <= 0:
            continue
        dist = bfs_dist(card, adj, n)
        for target in range(1, n + 1):
            if have[target] < need[target] and target in dist:
                transfers = min(extra, need[target] - have[target])
                total += transfers * dist[target]
                have[card] -= transfers
                have[target] += transfers
                extra -= transfers
                if extra == 0:
                    break

    print(total)
