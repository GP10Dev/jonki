import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            messagebox.showinfo("Stack", "Stack is empty. Cannot pop an item.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            messagebox.showinfo("Stack", "Stack is empty. No items to peek.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


def push_item():
    item = entry.get()
    stack.push(item)
    entry.delete(0, tk.END)
    update_stack_display()


def pop_item():
    popped_item = stack.pop()
    if popped_item is not None:
        messagebox.showinfo("Popped Item", f"Popped item: {popped_item}")
    update_stack_display()


def peek_item():
    top_item = stack.peek()
    if top_item is not None:
        messagebox.showinfo("Top Item", f"Top item: {top_item}")


def update_stack_display():
    stack_display.delete(1.0, tk.END)
    for item in reversed(stack.items):
        stack_display.insert(tk.END, item + "\n")


# Create a stack instance
stack = Stack()

# Create the main window
root = tk.Tk()
root.title("Stack")

# Create a frame to hold the stack display
frame_stack_display = tk.Frame(root)
frame_stack_display.pack(pady=10)

# Create a text widget to display the stack
stack_display = tk.Text(frame_stack_display, width=30, height=10)
stack_display.pack()

# Create a frame to hold the input field and buttons
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Create an entry field for input
entry = tk.Entry(frame_input, width=20)
entry.pack(side=tk.LEFT)

# Create a "Push" button
push_button = tk.Button(frame_input, text="Push", command=push_item)
push_button.pack(side=tk.LEFT, padx=5)

# Create a "Pop" button
pop_button = tk.Button(frame_input, text="Pop", command=pop_item)
pop_button.pack(side=tk.LEFT, padx=5)

# Create a "Peek" button
peek_button = tk.Button(frame_input, text="Peek", command=peek_item)
peek_button.pack(side=tk.LEFT)

# Run the GUI main loop
root.mainloop()
