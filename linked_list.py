class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next

        if current:
            prev.next = current.next
        else:
            print(f"Element {data} not found in the list.")

    def search(self, data):
        if self.is_empty():
            return False

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def display(self):
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage Example
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(5)

linked_list.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

linked_list.delete(20)
linked_list.display()  # Output: 5 -> 10 -> 30 -> None

print(linked_list.search(10))  # Output: True
print(linked_list.search(20))  # Output: False
