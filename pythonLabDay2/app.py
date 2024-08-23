# MAKE SURE EVERYTHING IS INSIDE A FUNCTION, in the lab only execute/comment the functions calls
from audioop import reverse
from curses.ascii import isdigit


# 1 - Fill an array of 5 elements from the user, Sort it in descending and ascending orders
# then display the output.
def fill_it():
  my_list = list()
  for i in range(5):
    user_input = input("type anything to append in the array!\n\t>> ")
    my_list.append(user_input) #this will sort lexicographically (alphabetically) 434534 < 523
    # my_list.append(int(user_input)) // will be sorted in ascending order due to int()
    print(f"original : {my_list}")
    # sorted(my_list)
    my_list.sort()
    print(f"sorted : {my_list}")
    my_list.reverse()
    print(my_list)



# 2 - Write a function that accepts two arguments (length, start) to generate an array of a
# specific length filled with integer numbers increased by one from start.

def myFunc(length, start):
  myList = list()
  while start < length:
    myList.append(start)
    start += 1
  print(myList)

myFunc(100,50)


# 3 - Write a program which repeatedly reads numbers until the user
# 	    enters “done”. Once “done” is entered, print out the total, count, and average of the
# 	    numbers.
# 	    If the user enters anything other than a number, detect their
#       mistake, print an error message and skip to the next number.
def validate_and_calc():
  mylist = list()
  while True:
    user_input = input("type the numbers you wish! \n\t>> ")
    if user_input == "done":
      break
    else:
      if user_input.isdigit():
        mylist.append(int(user_input))
      else:
        print("invalid input")
        print("TRY AGAIN")
  print(f"numbers are{mylist} ")
  summation=sum(mylist)
  print(f"total sum ={summation}")
  average  = sum(mylist) / len(mylist)
  print(f"average ={average}")

validate_and_calc()




# Bonus:
# 4 - discuss why dictionary key can only be an immutable type,
# why the set only accepts immutable types, how the set makes sure it has non-duplicates

# dictionary can't get hold of mutable types as they are stored inside a hashtable using a hash
# generated from a hash function that can't be repeated else collisions will occur and thus u
# need to store them in a linked lists or increase the memory space of the hashtable (trad-off)


# code snippets:
# a,b = [1,2,3]
# print(a)
# print(b)
#
# a,_,b = [1,2,3]
# print(a)
# print(b)
# a, *_, b = [1,2,3,43,45,12]
# print(a)
# print(b)


# def modify_int(x: int) -> int:
#   print(x)
#   x += 1
#   print(x)
#   return x
# y = 5
# y = modify_int(y)
# print(y)
