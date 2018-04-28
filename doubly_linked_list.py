# Doubly-linked lists
# Act like a singly linked list except it has two pointers, a pointer to the next node and a pointer to the previous
# node. Allowing the list be traversed in any direction. Having access to both nodes deletion operations are
# much easier

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        # self.head points to the first node
        self.head = None
        # self.tail points to the latest node added to the list
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    # Delete a node
    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        # if current (which points to the head) contains the data being deleted set self.head.prev = None
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        # if current (which points to the tail) contains the deltion data set self.tail.next = None
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        # Element's not at the head or the tail, loop through the nodes to find the node to delete
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1

    # Search the list
    def search(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False

    # iterate through the list
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    # Reverse the list
    def reverse(self):
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        # reverse the order of head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def print_forwards(self):
        for node in self.iter():
            print(node)

    def print_backwards(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    # Insert item at head of list
    def insert_head(self, data):
        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value
