class Stack:

   def __init__(self):
      self.stack = []
      self.size = 0;

   def isEmpty(self):
      return len(self.stack) == 0

   def push(self, item):
      self.stack.append(item)

   def peek(self):
      return self.stack[self.size - 1]


stack = Stack()
stack.push(str(1))
stack.push(str(2))
stack.push(str(3))
stack.push(str(4))
print("stack after popping an element: " + str(stack.stack))

