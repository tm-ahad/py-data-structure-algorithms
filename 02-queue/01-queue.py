from queue import Queue

# Initializing a queue
q = Queue(maxsize=10)

q.put('a')
q.put('b')
q.put('c')

print("\nFull: ", q.full())

print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


