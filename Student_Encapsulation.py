class Student:
    def __init__(self):
        self._name = None
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age

def main():
    student = Student()
    student.name = "John"
    student.age = -20  # This won't change the age since it's negative
    print("Name:", student.name)
    print("Age:", student.age)

if __name__ == "__main__":
    main()
