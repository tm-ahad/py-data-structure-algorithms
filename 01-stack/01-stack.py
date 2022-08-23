
from turtle import st


stack = []

# append() function to push
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
print('\nElements popped from stack:')

while (IndexError):
    try:
        print(stack.pop())
    except IndexError:
        break

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
