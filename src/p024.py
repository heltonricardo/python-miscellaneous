from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


dog = Dog()
print("Dog says:", dog.speak())

cat = Cat()
print("Cat says:", cat.speak())

cow = Cow()
print("Cow says:", cow.speak())
