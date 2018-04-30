# Circular lists
# A circular list is a special case of a linked list. It is a list where the endpoints are connected. That is, the
# last node in the list points back to the first node.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        self.tail = None
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    # Deleting nodes - we cannot loop until current becomes None, if you delete a nonexistent node
    # you run the risk of getting stuck in an infinite loop
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val


class PrintCircList:
    def __init__(self):
        print("--- Circle list start")
        cl = CircularList()
        cl.append('monkey')
        cl.append('fish')
        cl.append('cow')
        cl.append('owl')

        # testing the delete function - by deleting an item not in the list
        cl.delete('socks')
        # testing the delete function - by deleting an item in the list
        cl.delete('owl')
        # An exit condition is required when iterating through a circular list to prevent a loop.
        # A simple way to prevent a loop is to use a counter variable.
        counter = 0
        for cl in cl.iter():
            print(cl)
            counter += 1
            if counter > 10:
                break
        print('/--- Circle list end')
