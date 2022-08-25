class Dequeue:

   def __init__(self, k: int) -> None:

      if not not k:
         self.queue = [None] * k
         self.len = 0

      else:
         self.queue = []

      self.k = k
      self.front = 0

      for _ in range(self.k):
         self.dequeue()

   def size(self) -> int:
      return len(self.queue)

   def dequeue(self) -> None:

      del self.queue[self.size() - 1]

   def enqueue(self, item) -> None:

      try:
         self.queue.insert(0, item)
      except IndexError:
         print("Queue is full")

   def isfull(self) -> bool:

      return len(self.queue) == self.k

   def view(self) -> None:
      print(self.queue)


myDQ = Dequeue(6)

myDQ.enqueue(1)
myDQ.enqueue(2)
myDQ.enqueue(3)
myDQ.enqueue(4)
myDQ.enqueue(5)
myDQ.enqueue(6)

print(f"After enqueue in the queue {myDQ.view()}")
print('Queue is full' if myDQ.isfull() else "Queue isn't full")
print(f"length of the queue {myDQ.size()}")

myDQ.dequeue()
myDQ.dequeue()

print(f"After dequeue in the queue {myDQ.view()}")
print('Queue is full' if myDQ.isfull() else "Queue isn't full")
print(f"length of the queue {myDQ.size()}")
