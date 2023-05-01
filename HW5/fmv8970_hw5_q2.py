from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.my_max = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        temp = self.my_max
        if self.my_max is None:
            self.my_max = e
        elif e > self.my_max:
            self.my_max = e
        self.data.push((e, temp))



    def top(self):
        return self.data.top()[0]

    def pop(self):
        if self.top() == self.my_max:
            self.my_max = self.data.top()[1]                          # returning old max
        return self.data.pop()[0]

    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.my_max