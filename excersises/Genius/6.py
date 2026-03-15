#6

import sys
input = sys.stdin.readline

def dijkstra(start, graph, n):
    INF = 10**9
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[start] = 0

    for _ in range(n):
        u = -1
        min_dist = INF
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

S = int(input())
dirty_nodes = list(map(int, input().split()))

dist_map = {}
key_nodes = [S] + dirty_nodes
for node in key_nodes:
    dist_map[node] = dijkstra(node, graph, n)

current = S
visited_set = set()
visit_order = []
total = 0

while len(visit_order) < len(dirty_nodes):
    nearest = -1
    best = 10**9
    for d in dirty_nodes:
        if d not in visited_set:
            dist = dist_map[current][d]
            if dist < best:
                best = dist
                nearest = d
    total += best
    visited_set.add(nearest)
    visit_order.append(nearest)
    current = nearest

total += dist_map[current][S]
print(total)