"""
1 -
Class Person:
		attributes: name, age
		methods: say_hello, say_age

class SuperHero: that inherits from person
		 attributes += secret_identity, nemesis
		 methods: reveal_secret_identity, say_hello, old_say_age, say_age
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self):
    return f"hello from base class, name is {self.name}"
  def say_age(self):
    return f"hi from base class, age is {self.age}"

class SuperHero(Person):
  def __init__(self, name, age, secret_identity, nemesis):
    super().__init__(name, age)
    self.secret_identity = secret_identity
    self.nemesis = nemesis

  def reveal_secret_identity(self):
    return f"my identity is {self.secret_identity}"

  def my_nemesis(self):
    return f"this is my foe : {self.nemesis}"

  def say_old_age(self):
    return super().say_age()

  def say_new_age(self):
    return "my age is just a number haha!"

hero = SuperHero("ahmed", 24, "I am Batman", "joker")
print(hero.say_hello())#hello from base class, name is ahmed
print(hero.reveal_secret_identity())#my identity is I am Batman
print(hero.my_nemesis())#this is my foe : joker
print(hero.say_old_age())#hi from base class, age is 24
print(hero.say_new_age())#my age is just a number haha!
