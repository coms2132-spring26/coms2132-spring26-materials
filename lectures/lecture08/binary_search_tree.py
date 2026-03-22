


class BinarySearchTree:

    class Node:
        def __init__(self, element, left, right):
            self.element = element
            self.left = left
            self.right = right

        def __repr__(self): 
            return repr(self.element)
    
    def __init__(self):
        self.root = None
        self.size = 0

    def _find_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that 
        contains the element. If it doesn't exist, return None.
        """
        if node == None: 
            return None
        
        # node is not None
        if node.element < element: # node must be in right subtree
            return self._find_rec(node.right, element)
        elif node.element > element: # node must be in the left subtree
            return self._find_rec(node.left, element)
        else:  # now node.element must be == element
            return node

    def find(self, element):    
        # this method has been updated from the earlier version to return the _element_, not the Node object
        node = self._find_rec(self.root, element)
        if node == None:
            return None
        return node.element

    def _insert_rec(self, node, element):
        """
        Starting at the subtree rooted in node, find the node object that 
        contains the element. If it doesn't exist, return None.
        """
        if node is None: 
            return self.Node(element, None, None)
        
        # node is not None
        if node.element < element: # node must be in right subtree
            node.right = self._insert_rec(node.right, element)
        elif node.element > element: # node must be in the left subtree
            node.left = self._insert_rec(node.left, element)
    
        return node

    def insert(self, element):
        self.root = self._insert_rec(self.root, element)
        self.size += 1

    def _inorder(self):
        return self._inorder_rec(self.root)
    
    def _inorder_rec(self, node): # added 
        if node is None: 
            return []
        return self._inorder_rec(node.left) + [node.element] + self._inorder_rec(node.right)

    def __iter__(self):  # added 
        return iter(self._inorder)

    def __len__(self):  # added
        return self.size

if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert("A")
    bst.insert("B")
    bst.insert("C")
    bst.insert("D")

    bst.find("D")