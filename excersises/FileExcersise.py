with open("FileExcersise.txt", "w") as f1:
    f1.write("Hello world!" + '\n' + "hello")
    f1.close()

with open("FileExcersise.txt", "r") as f1:
    print(f1.read())
    for char in f1:
        data = char.strip().split(" ")
        print(data)
