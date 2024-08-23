from curses.ascii import isalpha

# Lab:
# 	- write a program that prints hello world
# print("hello world")

#===============================================
# 	- application to take a number in binary form from the user,
# and print it as a decimal
user_inp = input("Enter a number: ")
if all(char in '01' for char in user_inp):
  print(int(user_inp,2))
else:
  print("invalid input")

#or this solution

user_inp = input("Enter a number: ")
if len(user_inp) == user_inp.count('1')+user_inp.count('0'):
  print(int(user_inp,2))
else:
  print("invalid input")

#===============================================
# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
user_inp = input("Enter a number: ")
if user_inp.isdigit():
  user_inp= int(user_inp)
  if user_inp % 15 == 0:
    print("fizzbuzz")
  elif user_inp % 3 == 0:
    print("fizz")
  elif user_inp % 5 == 0:
    print("buzz")
else:
  print("invalid input")

#===============================================
# 	- Ask the user to enter the radius of a circle print its calculated area and circumference
r = float(input("Enter the radius of the circle: "))
#or  r = float(r)
if r >= 0 :
  area = 3.14 * r**2
  circum = 2 * 3.14 * r
  print("The area of the circle is:", round(area,2))
  print("The circumference is:", round(circum,2))
else:
  print("invalid input")
#===============================================
# 	- Ask the user for his name then confirm that he has entered
# 	his name (not an empty string/integers).
# 	then proceed to ask him for his email and print all this data
user_inp = input("Enter your name: ")
if len(user_inp) > 0:
  if user_inp.isalpha() :
    email = input("Please enter your email address")
    print(f"Thank you! your name is{user_inp}, your mail is {email} ")
  else:
    print("invalid input")
else:
  print("empty string")

#===============================================
# 	- Write a program that prints the number of times the
# 	substring 'iti' occurs in a string

x = "iti"
print(x.count('i'))
