# Write a program that uses abstraction. In object-oriented programing, abstraction is a mechanism that allows us to create classes and methods without specifying their behavior or value concretely.
# Algorithm: 1_Create an abstract class Animal with an abstract method sound. 2_Create the subclasses Dog and Cat that inherit from Animal and implement the sound method. 3_Create  objects from the Dog and Cat classes and print their sounds.

from abc import ABC, abstractmethod

#Abstract base class Animal with abstract method sound
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Subclass Dog inheriting from Animal, overriding the sound method
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
#Subclass Cat inheriting from Animal, overriding the sound method
class Cat(Animal):
    def sound(self):
        return "Meow!"
    

#Create objects from Dog and Cat classes
dog = Dog()
cat = Cat()


#Call the sound method of Dog and Cat objects
print(dog.sound())
print(cat.sound())