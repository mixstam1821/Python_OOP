class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def main():
    dog = Dog()
    cat = Cat()

    dog.make_sound()  # Output: Woof
    cat.make_sound()  # Output: Meow

if __name__ == "__main__":
    main()
