
# try:
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second number: "))
#     if num1 > num2:
#         print(f"{num1} > {num2}")
#     elif num2 > num1:
#         print(f"{num2} > {num1}")
#     else:
#         print(f"{num1} = {num2}")
#
# except ValueError:
#     print("can't use letters or symbols")
# except TypeError:
#     print("can't use Strings")


#make user create files by himself
try:
    file_name = input("Enter a file name to open: ")
    with open(file_name, "r+") as f1:
        f1.readline()
        text = input("Enter a text that you want to write in this file: ")
        f1.write(text + "\n")
        print("text added successfully")
except FileNotFoundError:
    with open(file_name, "w") as f1:
        print("file was not found, file created successfully")
        text = input("Enter a text that you want to write in this file: ")
        f1.write(text + "\n")
        print("text added successfully")

