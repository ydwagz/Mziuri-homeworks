# 1

with open("first numbers.txt", "r", encoding="utf-8") as f1, \
     open("Second numbers.txt", "w", encoding="utf-8") as f2:

    for line in f1:
        f1_pow = int(line) ** 2
        print(f1_pow)
        f2.write(str(f1_pow) + "\n")

print("--------------------")

#2

insert_a_year = input("Enter a year: ")

with open("oscars.txt", "r", encoding="utf-8") as f3:
    for line in f3:
        if insert_a_year in line:
            print(line)
