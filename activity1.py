#import neccessary Modules
from abc import ABC, abstractmethod

#create base class
class absclass(ABC):
    #function to print a value
    def print(self,x):
        print("passed value is:",x)
    #abstract method
    def task(self):
        print("We are inside absclass task")
#create subclass
class test_class(absclass):
    def task(self):
        print("We are inside the task_class task ")
#object of text class created
test_obj = test_class()
test_obj.task
test_obj.print(100)


     