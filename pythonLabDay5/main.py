"""
    class Person:
    Private Attributes:
        __name:
        __brith year:

    methods:
        say_hello: prints name whenever called

    properties:
        name
        age
"""
from datetime import date
class Person:
  def __init__(self, name, birthyear):
    self.__name = name
    self.__birthyear = birthyear
  @property
  def get_name(self):
    return self.__name

  def say_hello(self):
    print("Hello " + self.__name)
  def calc_age(self):
    today = date.today()
    return today.year - self.__birthyear
#implement property that returns age

myperson = Person("ahmed", 1999)
myperson.say_hello()
print(myperson.calc_age())
print(myperson._Person__name)
print(myperson.get_name)
