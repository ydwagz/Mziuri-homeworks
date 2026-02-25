class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(f"სახელი: {self.name}, გვარი: {self.surname}")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            removed = self.students.pop(index)
            print(f"წაიშალა: {removed.name} {removed.surname}")
        else:
            print("არასწორი ინდექსი")

    def show_students(self):
        for student in self.students:
            student.get_info()



school = School("მზიური", "ვაჯაფშაველას ქუჩა")


print("---------------")
print("მოსწავლეები")
print("---------------")
student1 = Student("ლუკა", "გოდაძე", 14)
student2 = Student("ჯასურბეკ", "აჰმედი", 67)
student3 = Student("ადოლფ", "ჰიტლერი", 69)


school.add_student(student1)
school.add_student(student2)
school.add_student(student3)


school.show_students()


school.remove_student(2)

print("---------------")
print("წაშლის შემდეგ:")
print("---------------")
school.show_students()