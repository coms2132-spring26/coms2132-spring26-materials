class List:
  """
  abstract data type for a list.
  """

  def get(k):  #retrieve element at index k
    pass

  def insert(k,x): #insert element x at index k 
    pass

  def remove(k):  #remove element at index k
    pass

  def append(x): # add x at the end of the list
    pass


class DoubleNode:
  
  def __init__(self, element, prev, next):
    self.element = element
    self.prev = prev
    self.next = next
    

class LinkedListIterator: 

  def __init__(self, current):
    self.current = current

  def next(self):
    if self.current.next == None: 
      raise StopIteration
    element = self.current.element
    self.current = current.next
    return element    


class DoubleLinkedList(List): 

  def __init__(self): 
    self._head = DoubleNode(None, None, None)
    self._tail = DoubleNode(None, self._head, None) 
    self._head.next = self._tail
    self.len = 0

  def iterator(self): 
    return LinkedListIterator(self._head.next)


  def get_node(self, k):
   
    if k == -1: 
      return self._head    

    if k <= self.len // 2:   # k in first half
      current = self._head.next
      for i in range(k):
        current = current.next
    else:                   # k in second half    
      current = self._tail.prev
      for i in range(self.len - k):
        current = current.prev
      

    return current

  def get(self, k):  #retrieve element at index k
    return self.get_node(k).element
   
  def insert(self, k,x): #insert element x at index k 
    if k > self.len: 
      raise IndexError("invalid list index") 

    pred = self.get_node(k-1)
    node = DoubleNode(x, None, None) 
    node.next = pred.next 
    pred.next = node
    node.next.prev = node
    node.prev = pred 
    self.len += 1

  def remove(self, k):  #remove element at index k
      if k >= self.len:
        raise IndexError("invalid list index")

      node = self.get_node(k)
      pred = node.prev
      succ = node.next

      pred.next = succ
      succ.prev = pred
      node.next = None
      node.prev = None
      self.len -= 1

  def remove_first(self): #aka pop
    self.remove(0)

  def remove_last(self): 
    self.remove(self.len - 1)

  def prepend(self, x): # insert at the beginning of list 
    self.insert(0, x)    

  def append(self,x): # add x at the end of the list, aka push
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
   


li = DoubleLinkedList()
li.append("A")
li.append("B")
li.append("C")
li.append("D")

print(li)

print(li.get(0))
print(li.get(1))
print(li.get(2))
print(li.get(3))
