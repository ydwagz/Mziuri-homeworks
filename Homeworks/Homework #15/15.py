#1
class Sports:
    outdoor = True
    def __init__(self, sports_name, sports_team):
        self.sports_name = sports_name
        self.sports_team = sports_team
#2

class Sports1:
    outdoor = True

    def __init__(self, sports_name, sports_team):
        self.sports_name = sports_name
        self.sports_team = sports_team

    #### Do not change before this

    # Write your code here...
    def print_info(self):
        print(f"{sports_name} - {sports_team}")


#3

class Plant:
    def __init__(self, scientific_name, climate):
        self.scientific_name = scientific_name
        self.climate = climate

class Lotus(Plant):
    pass

#4

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


class Dog(Animal):
    def make_sound(self):
        print(self.sound)

#5

# Add Your Code Here...
class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def see_credentials(self):
        return (self.__username, self.__password)
### DO NOT CHANGE BELOW THIS LINE

def test_answer(username, password):
    obj = Login(username, password)
    return obj.see_credentials()

#6


class Login1:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def see_credentials(self):
        return (self.__username, self.__password)

    ### Write Your Code Here ...
    def set_new_pass(self, new_pass):
        self.__password = new_pass

    def set_new_user(self, new_user):
        self.__username = new_user


### DO NOT CHANGE BELOW THIS LINE

def test_answer1(username, password, new_user, new_pass):
    obj = Login1(username, password)
    obj.set_new_pass(new_pass)
    obj.set_new_user(new_user)
    return obj.see_credentials()

# final 1

class Vehicle:
    def __init__(self, company, fuel_amt, mileage_per_litre):
        self.company = company
        self.fuel_amt = fuel_amt
        self.mileage_per_litre = mileage_per_litre


class Car(Vehicle):
    def run(self, distance_km):
        fuel_needed = distance_km / self.mileage_per_litre
        if self.fuel_amt >= fuel_needed:
            self.fuel_amt -= fuel_needed
            print("Ran Successfully")
        else:
            print("Not Enough Fuel")


# final 2

class System:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def login(self, user, passw):
        if self.__username == user and self.__password == password:
            print("Login Successful")
        else:
            print("Invalid Credentials")

# final 3

class Numbers:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class Calculator(Numbers ):
    def add(self):
        return sum(self.value1, self.value2)
    def multiply(self):
        return self.value1 * self.value2
    def subtract(self):
        return self.value1 - self.value2
