# difficulty medium

def Data_Store(email="Unknown", name="Unknown", surname="Unknown", age="Unknown", gender="Unknown", birthdate="Unknown", number="Unknown",):
    store = input("write a name of the file to open/store you'r info inside: ")
    count = 0
    for char in store:
        count += 1
    if count >= 30:
        print("file name cant be greater than 30 characters")
    else:
        info = {
            "email": email,
            "name": name,
            "birthdate": birthdate,
            "surname": surname,
            "age": age,
            "gender": gender,
            "Number": number,


        }

        email = input("Email: ")
        name = input("Name: ")
        birthdate = input("Birthdate: ")
        surname = input("Surname: ")
        age = input("Age: ")
        gender = input("Gender: ")
        number = input("Number: ")

        new_info = {
            "email": email,
            "name": name,
            "birthdate": birthdate,
            "surname": surname,
            "age": age,
            "gender": gender,
            "Number": number,
        }
        with open(store, "w+") as f1:
            for item in new_info.items():
                f1.write(str(item) + "\n")

        print(f"success, you can view your info in {store} file")

        return



print(Data_Store())









