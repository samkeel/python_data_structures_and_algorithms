class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

#Binary search tree
class Tree:
    def __init__(self):
        self.root_node = None

    # Find min, max and insert take O(h) where h is the height of the tree.
    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current

    # To make the binary tree searchable insert a mid value first then do a comparison operation anything
    # smaller values goes on the left larger values to the right.
    def insert(self, data):
        node = Node(data)
        # check to see if dealing with Root node
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                # Check if data in new node is less than current node.
                if node.data < current.data:
                    current = current.left_child
                    # Check if node has left child node. If not then insert new node, else keep traversing.
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
            return (parent, current)

    # Remove takes O(h) time
    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        # When the node has no children.
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        # When the node we want to delete has one child.
        elif children_count ==1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
        # When the node we want to delete has two children:
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
        if parent_of_leftmost_node.left_child == leftmost_node:
            parent_of_leftmost_node.left_child = leftmost_node.right_child
        else:
            parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child



class PrintBinTree:
    def __init__(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(2)
        tree.insert(7)
        tree.insert(9)
        tree.insert(1)

        for i in range(1, 10):
            found = tree.search(i)
            print("{}: {}".format(i, found))
