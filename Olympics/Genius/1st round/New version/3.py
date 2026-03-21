#3



from collections import deque

n = int(input())
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