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
import json

import queue


# import pickle (unsecure) - Deprecated
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
  @classmethod
  def save(cls):
    data = {name:(list(queue.queue) , queue.size) for name, queue in cls._instances.items()}
    with open("myfile.txt", "w") as file:
      json.dump(data, file)
      print("data saved")
  @classmethod
  def load(cls):
    with open("myfile.txt", "r") as file:
      data = json.load(file)
      cls._instances={}
      for name, (queue_data,size) in data.items():
        queue_instance = cls(name, size)
        queue_instance.queue = queue_data
        cls._instances[name]=queue_instance
      print("Queues loaded")


print("#" * 50)
class QueueOutOfRangeException(Exception):
  pass