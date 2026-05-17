# MoBot - AI smoking detection system

fined_today = set()


class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def __str__(self):
        return f'{self.name}, {self.age} წლის | ბალანსი: ₾{self.balance}'

    def fine(self):
        if self.balance >= 50:
            self.balance -= 50
            print(f'  ✓ ჯარიმა გადახდილია. ახალი ბალანსი: ₾{self.balance}')
        else:
            print(f'  ✗ არასაკმარისი თანხა (₾{self.balance}). გთხოვთ ეწვიოთ ახლო ბანკს.')


class Camera:
    def __init__(self, place, person: Person):
        self.place = place
        self.person = person

    def scan(self, smoking: bool):
        print(f'\n[MoBot] აფიქსირებს {self.place}ში...')
        if smoking:
            if self.person.name in fined_today:
                print(f'  ⚠ მოწევა დაფიქსირებულია! პიროვნება: {self.person.name}')
                print(f'  ⏭ უკვე გადახდილია, გამოტოვება.')
            else:
                print(f'  ⚠ მოწევა დაფიქსირებულია! პიროვნება: {self.person.name}')
                self.person.fine()
                fined_today.add(self.person.name)
        else:
            print(f'  ✓ No violation detected.')


def mobot(place, person, smoking):
    camera = Camera(place, person)
    camera.scan(smoking)


# --- Test ---
lasha = Person('ლაშა', 35, 200)
gela = Person('გელა', 22, 150)
luca = Person('ლუკა', 14, 67)


print(lasha)
mobot('თბილისი', lasha, True)
print("\n")
print(gela)
mobot('ბათუმი', gela, True)
print("\n")
print(lasha)
mobot('ქუთაისი', lasha, True)
print("\n")
print(luca)
mobot('ქუთაისი', luca, False)
print("\n")