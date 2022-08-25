import queue

class PriorityQueue:

   def __init__(self, k=False) -> None:

      if not not k:

         self.queue = [None] * k
      else:

         self.queue = []

      self.getindex = -1

      for _ in range(k):
         self.dequeue()

   def put(self, item) -> None:
      try:

         self.queue.append(item)
      except IndexError:

         print("Queue is full")

   def get(self) -> any:
       try:

          self.getindex = self.getindex + 1
          return self.queue[self.getindex]
       except IndexError:

          return None

   def size(self) -> int:
      return len(self.queue)

   def isfull(self) -> bool:
      return len(self.queue) == self.k

   def view(self) -> None:
      print(self.queue)

   def dequeue(self) -> None:

      del self.queue[self.size() - 1]


myPQ = PriorityQueue()

myPQ.put(1)
myPQ.put(2)
myPQ.put(3)
myPQ.put(4)

print(myPQ.get())

myPQ.dequeue()

print(myPQ.get())
print(myPQ.get())
print(myPQ.get())
