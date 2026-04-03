# classes_objects.py
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        print(self.name + " is studying")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Kevin", 20)
student2 = Student("Alice", 22)

print(student1.name)
print(student2.age)

student1.study()
student2.study()

student1.display()
student2.display()
