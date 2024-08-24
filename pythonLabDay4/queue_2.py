"""
3 - We need to implement another queue class that has the same properties as previous but with the following changes:
	A. The queue should have a name that is provided as a parameter for its initializer
	B. The queue should have a size that is provided as a parameter of its initializer
	   and if we tried to insert more values than its size raises a custom created exception called
	   QueueOutOfRangeException
	C. The Queue class keeps track of all queues instances that has been created through this class
	   and we can get any queue of them using its name
	D. The queue class should have two class methods called (save, load)
	   which saves all created queues instances to a file and load them when needed. (bonus)

"""

from collections import deque
import pickle
class Queue:
  _instances={} # this is a class variable
  def __init__(self, name, size):
    self.queue= deque()
    self.name=name
    self.size=size
    Queue._instances[name]=self

  def enqueue(self, value):
    if len(self.queue)<self.size:
      self.queue.append(value)
      print(f"{value} is added")
    else:
      raise QueueOutOfRangeException("Queue is full")
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
  ## bonus part (save and load)
  def save(self):
    with(open (self.name, "wb")) as file:
      pickle.dump(self.queue, file)
  def load(self):
    with(open(self.name, "rb")) as file:
      self.queue = pickle.load(file)


print("#" * 50)
class QueueOutOfRangeException(Exception):
  pass