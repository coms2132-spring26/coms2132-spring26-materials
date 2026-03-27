class List:
  """
  abstract data type for a list.
  """

  def get(self, k):  
    ''' retrieve element at index k
    '''
    pass

  def insert(self, k,x): 
    ''' insert element x at index k 
    '''
    pass

  def remove(self, k): 
    ''' remove element at index k
    '''
    pass

  def append(self, x): 
    ''' add x at the end of the list
    '''
    pass

  def __len__(self): 
    ''' return the length of the list
    '''
    pass


class DoubleNode:
  
  def __init__(self, element, prev, next):
    self.element = element
    self.prev = prev
    self.next = next
    

class DoubleLinkedList(List): 

  def __init__(self): 
    self._head = DoubleNode(None, None, None)
    self._tail = DoubleNode(None, self._head, None) 
    self._head.next = self._tail
    self.len = 0


  def _get_node(self, k):
    '''internal method to retrieve the node at index k
    '''
   
    if k == -1: 
      return self._head    

    if k <= self.len // 2:   # k in first half
      current = self._head.next
      for i in range(k):
        current = current.next
    else:                   # k in second half    
      current = self._tail.prev
      for i in range(self.len - k -1):
        current = current.prev
      
    return current


  def get(self, k):  
    ''' retrieve element at index k
    '''
    return self._get_node(k).element
   

  def insert(self, k,x): 
    '''insert element x at index k 
    '''
    if k > self.len: 
      raise IndexError("invalid list index") 

    pred = self._get_node(k-1)
    node = DoubleNode(x, None, None) 
    node.next = pred.next 
    pred.next = node
    node.next.prev = node
    node.prev = pred 
    self.len += 1


  def remove(self, k):  
    '''#remove element at index k
    '''
    if k >= self.len:
      raise IndexError("invalid list index")

    node = self._get_node(k)
    pred = node.prev
    succ = node.next

    pred.next = succ
    succ.prev = pred
    node.next = None
    node.prev = None
    self.len -= 1

  def append(self,x): 
    '''add x at the end of the list, aka push
    '''
    self.insert(self.len, x)

  def __repr__(self): 
    if self.len == 0:
      return "[ ]"

    current = self._head.next
    result = "["
    while current.next != self._tail: #for i in range(self.len):
      result = result + str(current.element) + " "
      current = current.next
    result = result + str(current.element) + "]"
    return result 

  def ___str___(self): 
    return repr(self)
  

  def __len__(self): 
    '''return the length of the list
    '''
    return self.len 

  def flip_pairs(self):
    '''flips each adjacent pair in the linked list. 
       Note: if the list has an odd number of elements, the last element 
       remains in its original place. 
    '''
    # part a)
    b = self._head.next
    while b != self._tail and b.next != self._tail:  
      a = b.prev
      c = b.next
      d = c.next
      
      #  A <-> B <-> C <-> D, we want to swap B and C
      a.next = c
      c.prev = a
      c.next = b
      b.prev = c
      b.next = d      
      d.prev = b
      b = d
    

  def __iter__(self): 
    '''
    Return a ListIterator instance. 
    '''
    return LinkedListIterator(self)
    

class LinkedListIterator: 
  
  def __init__(self, list):
    self.the_list = list  
    self.current = self.the_list._head.next

  def __next__(self):  # part b) 
    '''
    Return the next element from the iteration. If no more element is available, 
    the method should raise a StopIteration exception. 
    '''
    if self.current == self.the_list._tail: 
      raise StopIteration

    next_item = self.current.element
    self.current = self.current.next
    return next_item
    

"""
I used ChatGPT with the following prompt: 

Consider the following implementation of a doubly linked list. Write test cases to test the flip_pairs method and the iterator. 
[insert full linked_list code]

The initial output used pytest, which we didn't cover in class yet. so I asked "do not use pytest. Just include the test cases in the main."

I noticed that the iterator tests did not check nested loops, so I asked "add a test case to try nested iterators."

This resulted in the following code:
""" 


def main():
    # Helper functions
    def build_dll(items):
        dll = DoubleLinkedList()
        for x in items:
            dll.append(x)
        return dll

    def to_pylist(dll):
        return [x for x in dll]

    def assert_equal(actual, expected, msg=""):
        if actual != expected:
            raise AssertionError(f"{msg}\n  expected: {expected}\n  actual:   {actual}")

    def assert_raises(exc_type, func, msg=""):
        try:
            func()
        except exc_type:
            return
        except Exception as e:
            raise AssertionError(f"{msg}\n  expected exception {exc_type.__name__}, got {type(e).__name__}: {e}")
        else:
            raise AssertionError(f"{msg}\n  expected exception {exc_type.__name__}, but no exception was raised")

    # -----------------------
    # flip_pairs tests
    # -----------------------

    dll = build_dll([])
    dll.flip_pairs()
    assert_equal(to_pylist(dll), [], "flip_pairs on empty list failed")
    assert_equal(len(dll), 0, "length wrong after flip_pairs on empty list")

    dll = build_dll([1])
    dll.flip_pairs()
    assert_equal(to_pylist(dll), [1], "flip_pairs on single-element list failed")
    assert_equal(len(dll), 1, "length wrong after flip_pairs on single-element list")

    dll = build_dll([1, 2])
    dll.flip_pairs()
    assert_equal(to_pylist(dll), [2, 1], "flip_pairs on two-element list failed")
    assert_equal(len(dll), 2, "length wrong after flip_pairs on two-element list")

    dll = build_dll([1, 2, 3, 4, 5])
    dll.flip_pairs()
    assert_equal(to_pylist(dll), [2, 1, 4, 3, 5], "flip_pairs on odd-length list failed")
    assert_equal(len(dll), 5, "length wrong after flip_pairs on odd-length list")

    dll = build_dll([10, 20, 30, 40])
    dll.flip_pairs()
    assert_equal(to_pylist(dll), [20, 10, 40, 30], "flip_pairs on even-length list failed")
    assert_equal(len(dll), 4, "length wrong after flip_pairs on even-length list")

    items = [1, 2, 3, 4, 5, 6]
    dll = build_dll(items)
    dll.flip_pairs()
    dll.flip_pairs()
    assert_equal(to_pylist(dll), items, "flip_pairs twice should restore original order")

    # -----------------------
    # iterator tests
    # -----------------------

    dll = build_dll([])
    it = iter(dll)
    assert_raises(StopIteration, lambda: next(it), "iterator should StopIteration on empty list")

    dll = build_dll([1, 2, 3])
    assert_equal([x for x in dll], [1, 2, 3], "iterator did not yield elements in order")

    dll = build_dll([7, 8])
    it = iter(dll)
    assert_equal(next(it), 7, "iterator first element incorrect")
    assert_equal(next(it), 8, "iterator second element incorrect")
    assert_raises(StopIteration, lambda: next(it), "iterator should StopIteration after exhaustion")

    dll = build_dll([1, 2, 3])
    it1 = iter(dll)
    it2 = iter(dll)
    assert_equal(next(it1), 1, "it1 first element incorrect")
    assert_equal(next(it1), 2, "it1 second element incorrect")
    assert_equal(next(it2), 1, "it2 should be independent of it1 (first)")
    assert_equal(next(it2), 2, "it2 should be independent of it1 (second)")
    assert_equal(next(it2), 3, "it2 third element incorrect")
    assert_raises(StopIteration, lambda: next(it2), "it2 should StopIteration after exhaustion")

    dll = build_dll([1, 2, 3, 4, 5])
    dll.flip_pairs()
    assert_equal([x for x in dll], [2, 1, 4, 3, 5], "iterator after flip_pairs yielded wrong order")

    # -----------------------
    # nested iterator test (for x in dll: for y in dll: ...)
    # -----------------------
    dll = build_dll([1, 2, 3])
    pairs = []
    for x in dll:
        for y in dll:   # this creates a NEW iterator each time; should restart from the head
            pairs.append((x, y))

    expected_pairs = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
    ]
    assert_equal(pairs, expected_pairs, "nested iteration produced incorrect pairs")

    print("All tests passed!")


if __name__ == "__main__":
    main()
