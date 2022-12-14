
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value, next) -> None:
        self.value = value
        self.next = Node(next)
        self.tail = self

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
        size: int = 1
        curr = self

        while not not curr.next:
            curr = curr.next
            size = size + 1

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
        self.tail.next = Node(item)
        self.tail = self.tail.next

    def replaceAt(self, index, item):
        NODES = self.getNodeByIndex(index)
        node = self.getNodeByIndex(index - 1)
        node.value = item
        node.next = NODES


myLinkedList = LinkedList(3, 4)
myLinkedList.insert(5)
myLinkedList.insert(6)
myLinkedList.insert(7)
myLinkedList.insertAt(2, 8)


myLinkedList.view()
print(myLinkedList.getIndex(5))
