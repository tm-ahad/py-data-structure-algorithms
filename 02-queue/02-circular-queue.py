
from operator import le
from select import select


class CircularQueue:

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

    def enqueue(self, item) -> None:
        try:
            queueLen = len(self.queue)
            self.queue.append(item)
            self.len = self.len + 1
        except IndexError:
            print("Queue is full")

    def dequeue(self) -> None:
        self.len = self.len - 1
        del self.queue[0]

    def isFull(self) -> bool:
        return self.k == len(self.queue)

    def view(self) -> None:
        print(self.queue)

    def size(self) -> int:
        return len(self.queue)


myCQ = CircularQueue(6)

myCQ.enqueue(1)
myCQ.enqueue(2)
myCQ.enqueue(3)
myCQ.enqueue(4)
myCQ.enqueue(5)
myCQ.enqueue(6)

print(f"After enqueue in the queue {myCQ.view()}")
print('Queue is full' if myCQ.isFull() else "Queue isn't full")
print(f"length of the queue {myCQ.size()}")

myCQ.dequeue()
myCQ.dequeue()

print(f"After dequeue in the queue {myCQ.view()}")
print('Queue is full' if myCQ.isFull() else "Queue isn't full")
print(f"length of the queue {myCQ.size()}")
