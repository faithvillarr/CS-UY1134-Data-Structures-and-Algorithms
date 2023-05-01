# Define a LinkedQueue class that implements the Queue ADT
from DoublyLinkedList import DoublyLinkedList

# queue is fifo. so enqueue adds to back. dequeue pulls from the front


class LinkedQueue:

    def __init__(self):
        self.data_dll = DoublyLinkedList()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        self.data_dll.add_last(elem)
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        res = self.data_dll.delete_first()
        self.n -= 1
        return res

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_dll.header.next.data
