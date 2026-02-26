class AbstractPosition:
    'An abstraction representing the location of a single element'

    def element(self):
        raise NotImplemented('Must be implemented by a subclass')

    def __eq__(self, other):
        'Returns True if Position represents the same location'
        raise NotImplemented('Must be implemented by a subclass')

    def __ne__(self, other):
        return not (self == other)

class AbstractTree:

    def root(self):
        'Return the root of the tree or None'
        raise NotImplemented('Must be implemented in subclass')

    def parent(self, p):
        'Return the parent of the node at position p or none if p is root'
        raise NotImplemented('Must be implemented in subclass')

    def children(self, p):
        'Return all children of the node at position p'
        raise NotImplemented('Must be implemented in subclass')

    def num_children(self, p):
        'Return the number of children of the node at position p'
        raise NotImplemented('Must be implemented in subclass')

    def __len__(self):
        'Return the number of elements in the tree'
        raise NotImplemented('Must be implemented in subclass')

    # Query methods
    
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

class AbstractBinaryTree(AbstractTree):
    def left(self, p):
        'Return the left child of node at position p'
        raise NotImplemented('Must be  implemented by subclass')

    def right(self, p):
        'Return the right child of node at position p'
        raise NotImplemented('Must be  implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        children = []
        if self.left(p) is not None:
            children.append(self.left(p))
            
        if self.right(p) is not None:
            children.append(self.right(p))
        return children
    
class ArrayBinaryTree(AbstractBinaryTree):

    class Position(AbstractPosition):
        def __init__(self, container, idx):
            self._container = container # This is a reference to the tree containing the node
            self._idx = idx
        
        def element(self):
            return container._data[self.idx]

        def __eq__(self, other):
            return type(other) is type(self) and other._idx is self._idx


    def _make_position(self, idx):
        "Converts a node idx to the node's position in the tree"    
        return self.Position(self, idx)

    def _validate(self, p): # retrieve the idx in position p 
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')        
        return p._idx

    def __init__(self): # init of ArrayBinaryTree

        self._size = 0
        self.CAPACITY = 10
        self._data = [None] * self.CAPACITY

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(1)

    def parent(self, p):
        'Return the parent of the node at position p or none if p is root'
        idx = self._validate(p)
        return self._make_position(idx // 2)

    def left(self, p):
        idx = self._validate(p)
        return self._make_position(idx  * 2)

    def right(self, p):
        idx = self._validate(p)
        return self._make_position(idx * 2 + 1)

    # Constant time operation
    def _add_root(self, e):        
        self._size = 1
        self._data[1] = e
        return self._make_position(1)

    # Constant-time operation
    def _add_left(self, p, e):
        idx = self._validate(p)
        self._size += 1
        
        self.ensure_capacity(2*idx)
        self._data[2*idx] = e
        return self._make_position(2 * idx)

    # Constant-time operation
    def _add_right(self, p, e):
        idx = self._validate(p)        
        self._size += 1
        self.ensure_capacity(2*idx+1)
        self._data[2 * idx + 1] = e
        return self._make_position(2 * idx + 1)

    def ensure_capacity(self, capacity): 
        if len(self._data) < capacity: 
            new_data = [None] * (len(self._data) * 2)
            for i in range(len(self._data)):
                new_data[i] = self._data[i]
            self._data = new_data