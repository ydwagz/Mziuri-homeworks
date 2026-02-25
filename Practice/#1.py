#1

f1 = open("First number.txt", "r", encoding="utf-8")
First_numbers = (f1.read())

f2 = open("second number.txt", "a", encoding="utf-8")
#pow(First_numbers, 2)
print(First_numbers)

f2.close()
