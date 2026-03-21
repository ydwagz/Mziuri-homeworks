# #1

days = int(input("Enter the number of days: "))
co2 = list(map(int, input("Enter the CO2 level: ").split()))

total_co2 = sum(co2)
if total_co2 > days:
    print("error: total CO2 cannot be greater than number of days")
else:
    average_co2 = total_co2 / len(co2)
    count = 0
    for i in co2:
        if i > average_co2:
            count += 1
    print(f"total days: {days}")
    print(f"average: {average_co2}")
    print(f"number of days above average: {count}")

print("-----------------------------")

#2

n = int(input("number of days: "))

max_val = -1
min_val = float('inf')
max_idx = 1
min_idx = 1

for i in range(1, n + 1):
    capacity, fill_percent = map(int, input("Capacity, fill percent: ").split())
    value = capacity * fill_percent

    if value > max_val:
        max_val = value
        max_idx = i

    if value < min_val:
        min_val = value
        min_idx = i

print(f"Most full: {max_idx}")
print(f"Most empty: {min_idx}")

print("-----------------------------")
#3



from collections import deque

n = int(input("size: "))
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    while len(row) < n:
        row += list(map(int, input().split()))
    grid.append(row)

queue = deque()
dist = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            queue.append((i, j))
            dist[i][j] = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
max_dist = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            max_dist = max(max_dist, dist[nx][ny])
            queue.append((nx, ny))

print(max_dist)


print("-----------------------------")
#4

glass = 0
metal = 0
plastic = 0
n = int(input("number of items: "))
for i in range(1, n + 1):
    types, weight = input().split()
    weight = float(weight)
    if types == 'P':
        plastic += weight
    elif types == 'M':
        metal += weight
    elif types == 'G':
        glass += weight

sum_weights = plastic + metal + glass
plastic_percent = (plastic / sum_weights) * 100
metal_percent = (metal / sum_weights) * 100
glass_percent = (glass / sum_weights) * 100
print(f"Plastic: {plastic}kg. {plastic_percent:.2f}%")
print(f"Metal: {metal}kg. {metal_percent:.2f}%")
print(f"Glass: {glass}kg. {glass_percent:.2f}%")

print("-----------------------------")
#5

n, k = map(int, input("budget, available panels: ").split())
panels = [tuple(map(int, input("Panels: ").split())) for _ in range(n)]
max_energy = [0] * (k + 1)

for price, energy in panels:
    for w in range(k, price - 1, -1):
        max_energy[w] = max(max_energy[w], max_energy[w - price] + energy)

print(max_energy[k])

print("-----------------------------")
#6


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

start_line = input().split()
S = int(start_line[1])
dirty_line = input().split()
dirty_nodes = list(map(int, dirty_line[1:]))
dist_map = {}
key_nodes = [S] + dirty_nodes

for node in key_nodes:
    dist_map[node] = dijkstra(node, graph, n)


current = S
visited = []
total = 0

while len(visited) < len(dirty_nodes):
    nearest = -1
    best = 10**9

    for d in dirty_nodes:
        if d not in visited:
            dist = dist_map[current][d]
            if dist < best:
                best = dist
                nearest = d

    total += best
    visited.append(nearest)
    current = nearest


total += dist_map[current][S]

print(total)