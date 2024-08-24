"""2 - A Queue is a linear structure which follows a particular order in which the operations are performed.
The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a
resource where the consumer that came first is served first.

We need to implement a python class that represents the queue data structure:

	The class should have these operations:
		- enqueue(value) => inserts a new value at the rear of the queue
		- dequeue() 	 => returns and removes a value from the front of the queue.
				    We should return None and print a warning message if we tried to pop value from an empty queue
		- is_empty() 	 => which returns True or False to represent whether the queue is empty or not
"""

from collections import deque
class Queue:
  def __init__(self):
    self.queue= deque()
  def enqueue(self, value):
    self.queue.append(value)
    print(f"{value} is added")
  def dequeue(self):
    if len(self.queue) == 0:
      print("you can't dequeue from an empty queue")
      return None
    else:
      print(f"{self.queue[0]} is removed")
      return self.queue.popleft()
  def is_empty(self):
    return len(self.queue) == 0
  def peek(self):
    if len(self.queue) == 0:
      print("you can't peek from an empty queue")
    else:
      return f"element on top is {self.queue[0]}"
  def display(self):
    return self.queue
  def display_queue_methods(self):
    return dir(self.queue)



my_queue = Queue()
my_queue.enqueue(5)#5 is added
my_queue.enqueue(6)#6 is added
my_queue.enqueue(7)#7 is added
my_queue.enqueue(8)#8 is added
my_queue.enqueue(9)#9 is added
my_queue.enqueue(10)#10 is added
my_queue.enqueue(11)#11 is added
print(my_queue.peek())#element on top is 5
my_queue.dequeue() #5 is removed
print(my_queue.display())#deque([6, 7, 8, 9, 10, 11])
