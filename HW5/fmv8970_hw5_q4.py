from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.og_stack = ArrayStack()   #main
        self.res_stack = ArrayStack()   #storage

    def __len__(self):
        return len(self.og_stack) + len(self.res_stack)

    def is_empty(self):
        return self.og_stack.is_empty() and self.res_stack.is_empty()

    def enqueue(self, item):
        self.og_stack.push(item)

    def dequeue(self):
        if not self.res_stack.is_empty():
            return self.res_stack.pop()
        else:
            for i in range(len(self.og_stack)):
                self.res_stack.push(self.og_stack.pop())
            return self.res_stack.pop()

    def first(self):
        if self.og_stack.is_empty():
            return self.res_stack.top()
        else:
            while not self.og_stack.is_empty():
                self.res_stack.push(self.og_stack.pop)
            return self.res_stack.top()


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.first())
    print(q.dequeue())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

main()