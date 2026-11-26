#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):
    #abstract method
    #should be implemented by all subclasses
    def move(self):
        pass
#subclasses
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
     print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
#driver code
r = Human()
r.move()

k = Snake()
k.move()

r = Dog()
r.move()

k = Lion()
k.move()
