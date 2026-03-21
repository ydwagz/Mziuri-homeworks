#2

n = int(input("number of days: "))

max_val = -1
min_val = float('inf')
max_idx = 1
min_idx = 1

for i in range(1, n + 1):
    capacity, fill_percent = map(int, input().split())
    value = capacity * fill_percent

    if value > max_val:
        max_val = value
        max_idx = i

    if value < min_val:
        min_val = value
        min_idx = i

print(f"Most full: {max_idx}")
print(f"Most empty: {min_idx}")