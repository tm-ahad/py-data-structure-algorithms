
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value, next) -> None:
        self.value = value
        self.next = Node(next)
        self.tail = self.getNodeByIndex(self.size() - 1)
        self.tail.next = self

    def getNodeByIndex(self, index) -> any:
        val = self
        i = index

        while True:
            if i > 0:
                val = val.next
                i = i - 1
            else:
                break

        return val

    def size(self) -> int:
        size: int = 0
        curr = self

        while True:
            try:
                curr = curr.next
                size = size + 1
            except AttributeError:
                break

        return size

    def view(self) -> None:
        ret = ""
        for i in range(self.size()):
            ret = f"{ret}{self.getNodeByIndex(i).value} -> "
        ret = f"{ret} None"
        print(ret)

    def getIndex(self, item) -> None:
        for i in range(self.size()):
            if (self.getNodeByIndex(i) == item):
                return i

    def insert(self, item):
        NODES = self.next
        self.next = Node(item)
        self.next.next = NODES


myLinkedList = LinkedList(3, 4)
myLinkedList.insert(5)
myLinkedList.insert(6)
myLinkedList.insert(7)
myLinkedList.insert(8)

print(myLinkedList.tail.next.value)
