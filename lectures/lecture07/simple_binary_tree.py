class _Node:

    def __init__(self, element, left = None, right = None):
        self.element = element        
        #self.children = children
        self.left = left
        self.right = right

class Tree: 

    def __init__(self, root):
        self.root = root


    def _height(self, node):
        print(node)
        # Define height of an emptry tree (i.e. node is None) as -1
        if node == None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

        #if node.left == None and node.right == None:
        #    return 0 
        #
        #max_height = 0 
        #if node.left != None: 
        #    left_height = self._height(node.left)
        #    if left_height > max_height: 
        #        max_height = left_height
        #
        #if node.right != None: 
        #    right_height = self._height(node.right)
        #    if right_height > max_height:
        #        max_height = right_height

        return max_height + 1
    
    def height(self):
        return self._height(self.root)

    def _postfix(self, node):
        if node == None: 
            return '' # empty string
        
        left_postfix = self._postfix(node.left)
        right_postfix = self._postfix(node.right)
        return left_postfix + ' '+ node.element+ ' '+ right_postfix  



    def postfix(self):
        return self._postfix(self.root)



if __name__ == "__main__":

    a = _Node("12")
    b = _Node("7")
    c = _Node("+", a, b)
    d = _Node("2")
    e = _Node("*", c, d)

    tree = Tree(e)
    print(tree.height())
    print(tree.postfix())

    #      *
    #     /  \
    #    +    2
    #  /   \
    # 12    7

    # Postfix: 12 7 + 2 *

        


