
class Node:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def _find_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that 
        contains the element. If it doesn't exist, return None.
        """
        print("Visiting ", node.element)
        if node is None: 
            return None
        
        # node is not None
        if node.element < element: # node must be in right subtree
            self._find_rec(node.right, element)
        elif node.element > element: # node must be in the left subtree
            self._find_rec(node.left, element)
        else:  # now node.element must be == element
            return node

    def find(self, element):    
        return self._find_rec(self.root, element)

    def _insert_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that 
        contains the element. If it doesn't exist, return None.
        """
        if node is None: 
            return Node(element, None, None)
        
        # node is not None
        if node.element < element: # node must be in right subtree
            node.right = self._insert_rec(node.right, element)
        elif node.element > element: # node must be in the left subtree
            node.left = self._insert_rec(node.left, element)
    
        return node

    def insert(self, element):
        self.root = self._insert_rec(self.root, element)


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert("A")
    bst.insert("B")
    bst.insert("C")
    bst.insert("D")

    bst.find("D")