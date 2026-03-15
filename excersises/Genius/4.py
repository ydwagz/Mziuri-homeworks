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
if plastic > glass > metal:
    print(f"Most common: {plastic}")
elif metal > glass > metal:
    print(f"Most common: {metal}")
elif glass > plastic > metal:
    print(f"Most common: {glass}")
print(f"Plastic: {plastic}kg {round(plastic_percent, 1):.2f}%")
print(f"Glass: {metal}kg {round(glass_percent, 1):.2f}%")
print(f"Metal: {metal}kg {round(metal_percent, 1):.2f}%")