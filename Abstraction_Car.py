from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, color):
        print("Car constructor called")
        self.color = color

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_color(self):
        return self.color

class Audi(Car):
    def __init__(self, color, speed):
        super().__init__(color)
        print("Audi constructor called")
        self.speed_val = speed

    def speed(self):
        return self.speed_val

    def __str__(self):
        return "Audi Color: " + self.color + " speed: " + str(self.speed())

class Mercedes(Car):
    def __init__(self, color, distance, time):
        super().__init__(color)
        print("Mercedes constructor called")
        self.distance = distance
        self.time = time

    def speed(self):
        return self.distance / self.time

    def __str__(self):
        return "Mercedes color is " + self.color + " and speed is : " + str(self.speed())

def main():
    s1 = Audi("Red", 2.2)
    s2 = Mercedes("Yellow", 2, 4)

    print(s1)
    print(s2)

if __name__ == "__main__":
    main()
