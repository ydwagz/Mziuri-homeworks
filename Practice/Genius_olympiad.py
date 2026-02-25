def Number_Check(num1, num2):
    if num1 == num2:
        result =  (2 * (num1 + num2))
        print(result)
    else:
        result = (num1 + num2)
        print(result)

Number_Check(2,2)

def recycle(item, weight):
    item = item
    if item == "Plastic bottle":
        price = 0.5
        result = price * weight
        print(f"${result}")
    elif item == "aluminum cans":
        price = 0.10
        result = price * weight
        print(f"${result}")
    elif item == "glass bottle":
        price = 0.20
        result = price * weight
        print(f"${result}")

recycle("glass bottle", 10)

def Find_triplets(*args):
    for num in set(args):
        if args.count(num) == 3:
            print("triplets found")



Find_triplets(5, 5, 3, 2, 8, 5)


