from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque


class MidStack(): #LILO but with midpush
    def __init__(self):
        self.s = ArrayStack()
        self.dq = ArrayDeque()

    def __len__(self):
        return len(self.s) + len(self.dq)

    def is_empty(self): #constant
        return len(self.dq) == len(self.s) == 0

    def push(self, e): # puts val on top of stack
        self.dq.enqueue_last(e)
        if (len(self.dq) + len(self.s)) // 2 < len(self.dq):
            temp = self.dq.dequeue_first()
            self.s.push(temp)

    def top(self):  # might need to change
        return self.dq.last()

    def pop(self):
        res = self.dq.dequeue_last()        # to be returned at a later date >:)
        while len(self.s) > len(self.dq):      # moves it over if the stack is too big
            temp = self.s.pop()
            self.dq.enqueue_first(temp)
        return res

    def mid_push(self, e):
        self.dq.enqueue_first(e)
        if (len(self.dq) + len(self.s)) // 2 + 1 < len(self.dq):
            temp = self.dq.dequeue_first()
            self.s.push(temp)


