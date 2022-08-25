
class Node:

   def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:

   def __init__(self, value, next) -> None:
      self.value = value
      self.next = Node(next)

   def getByIndex(self, index) -> any:
      val = self
      i = index

      while True:
         if i > 0:
            val = val.next
            i = i - 1
         else:
            break

      return val.value

   def size(self) -> int:
      size: int = 1
      curr = self

      while not not curr.next:
         curr = curr.next
         size = size + 1

      return size

   def view(self) -> None:
      ret = ""
      for i in range(self.size()):
         ret = f"{ret}{self.getByIndex(i)} -> "
      ret = f"{ret} None"
      print(ret)

   def getIndex(self, item) -> None:
      for i in range(self.size()):
         if (self.getByIndex(i) == item):
            return i


myLinkedList = LinkedList(3, 4)
myLinkedList.next.next = Node(5)

myLinkedList.view()
print(myLinkedList.getIndex(5))
