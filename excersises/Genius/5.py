#5

n, k = map(int, input("budget, available panels: ").split())
panels = [tuple(map(int, input("Panels: ").split())) for _ in range(n)]
max_energy = [0] * (k + 1)

for price, energy in panels:
    for w in range(k, price - 1, -1):
        max_energy[w] = max(max_energy[w], max_energy[w - price] + energy)

print(max_energy[k])