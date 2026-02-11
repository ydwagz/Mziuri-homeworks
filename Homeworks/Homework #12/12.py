#1
print("----------------")

correct = 0
while correct == 0:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    try:
        result = num1/num2
        print(result)
    except ValueError as message:
        print("You can't use letters or symbols")

    except ZeroDivisionError as message:
        print("You can't divide by zero")

    else:
        correct += 1
        while correct == 1:
            #2
            print("----------------")
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            try:
                result = num1/num2
                print(result)
            except ZeroDivisionError as message:
                print("You can't use letters or symbols")

            except ValueError as message:
                print("You can't use letters or symbols")

            else:
                correct += 1
                #3
                print("----------------")
                while correct == 2:
                    try:
                        my_list = ["shawarma", "kebab"]
                        print(my_list)
                        x = int(input("Enter a number: "))
                        print(my_list[x])
                    except IndexError as message:
                        print("Invalid Index")
                    except ValueError as message:
                        print("You can't use letters or symbols")

                    else:
                        correct += 1
                        while correct == 3:
                            try:
                                f1 = open("readMe.txt", "r")
                            except FileNotFoundError as message:
                                print("File not found")
                                break

                            else:
                                correct += 1
                                #6
                                print("----------------")
                                try:
                                    a = int(input("Enter a number: "))
                                    b = int(input("Enter a number: "))
                                    c = int(input("Enter a number: "))

                                    if a + b > c or a + c > b or b + c > a or a == b ==c:
                                        print("this triangle is possible to make")

                                except ValueError as message:
                                    print("You can't use letters or symbols")
                                    break








