#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())    # Output: Bark
print(garfield.sound()) # Output: Meow

# This will raise an error
animal = Animal()
print(animal.sound())
