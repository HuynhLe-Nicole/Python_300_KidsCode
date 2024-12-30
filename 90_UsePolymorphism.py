# Write a program that utilizes polymorphism. It is a mechanism that allows us to use a method in multiple forms.
#Algorithm: 1_Create a class Animal with a method sound. 2_Create subclasses Dog and Cat that inherit from Animal and override the sound method. 3_Create objects from the Dog and Cat classes and print out their sounds.

class Animal:
    def sound(self):
        return"Animal makes a sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return"Meow!"
    
#Create a list of Animal objects
animals = [Dog(), Cat()]

#Print the sound of each Animal in the list
for animal in animals:
    print(animals.sound())