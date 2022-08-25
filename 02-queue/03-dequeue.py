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

   def size(self):
      return len(self.queue)

   def dequeue(self):

      del self.queue[self.size() - 1]
