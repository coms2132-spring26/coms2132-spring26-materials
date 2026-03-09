class _Node:

    def __init__(self, element, left = None, right = None):
        self.element = element                
        self.left = left
        self.right = right

class Tree: 

    def __init__(self, root):
        self.root = root

    def postfix(self):
        return self._postfix(self.root)

    def _postfix(self, node):
        if node == None: 
            return '' # empty string
        
        left_postfix = self._postfix(node.left)
        right_postfix = self._postfix(node.right)
        return left_postfix + ' '+ right_postfix  + ' '+ node.element

    def infix(self):
        return self._infix(self.root)

    def _infix(self, node):
        if node == None: 
            return '' # empty string
        
        left = self._infix(node.left)
        right = self._infix(node.right)
        if node.element in "+-":
            return "("+left + ' '+ node.element +' '+ right+")"
        else:
            return left + ' '+ node.element +' '+ right


    def evaluate(self): 
        return self._evaluate(self.root)

    def _evaluate(self, node):
        if node.element == "+":
            return self._evaluate(node.left) + self._evaluate(node.right)
        elif node.element == "-":
            return self._evaluate(node.left) - self._evaluate(node.right)
        elif node.element == "*":
            return self._evaluate(node.left) * self._evaluate(node.right)
        elif node.element == "/":
            return self._evaluate(node.left) / self._evaluate(node.right)
        else: 
            return float(node.element) # Leaf node is a number. 
        
        # Note, that the base case is a leaf in this case.
    



def expression_tree_from_postfix(postfix):

    stack = []

    for c in postfix: 

        if c in "+-/*": # operator
            right = stack.pop()
            left = stack.pop()
            new_subtree = _Node(c, left, right)
            stack.append(new_subtree)

        else: # operand
            stack.append(_Node(c)) # append = push
    
    return Tree(stack.pop())



if __name__ == "__main__":

    #a = _Node("12")
    #b = _Node("7")
    #c = _Node("+", a, b)
    #d = _Node("2")
    #e = _Node("*", c, d)

    postfix = "12 7 + 2 *".split()
    tree = expression_tree_from_postfix(postfix)
    #print(tree.height())
    print(tree.postfix())
    print(tree.infix())
    print(tree.evaluate())

    #      *
    #     /  \
    #    +    2
    #  /   \
    # 12    7
  
    # Postfix: 12 7 + 2 *

    (12 + 7) * 2




