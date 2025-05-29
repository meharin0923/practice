#hidding unneccessary data and shows required data
'''three main rules:
*for abstract method there is no body.
*for abstract class no object is created.
*a class is konown as abstract class.if there is one or more abstract method.'''
#abc refer to abc module which provide abstract base classes(abcs)

#ex:
'''from math import sqrt,gcd
print(sqrt(36))
print(gcd(4,8))'''

#code:
from abc import ABC,abstractmethod
class car(ABC):#taken from the abc
    @abstractmethod#called as decorators
    def milage(self):#normal class if @.....method.. is added then its abstractclass which is placed before the defination
        pass
class bmw(car):
    def milage(self):
        print("it give 40kmph")
class audi(car):
    def milage(self):
        print("it gives 70kmph")
audi().milage()
bmw().milage()