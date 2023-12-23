class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def push(self, value):
        if len(self.items) < self.limit:
            self.items.append(value)
        else:
            print("Stack overflow: Unable to push element, the stack is full.")

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack underflow: Unable to pop element, the stack is empty.")
         
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty, cannot peek.")
          

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1  
