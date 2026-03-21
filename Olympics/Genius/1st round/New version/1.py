#1

days = int(input())
co2 = list(map(int, input().split()))

total_co2 = sum(co2)
average_co2 = total_co2 / len(co2)
count = 0
for i in co2:
    if i > average_co2:
        count += 1
print(f"Total: {days}")
print(f"average: {average_co2}")
print(f"number of days above average: {count}")