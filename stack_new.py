class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop an item.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No items to peek.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# Usage Example
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
