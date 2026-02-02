def binary_search(arr, x):
  left = 0
  right = len(arr)-1
    
  mid = (left + right) // 2
  while left<=right and arr[mid] != x:
      if arr[mid] > x: # x must be located in the first half
        #arr[mid].__gt__(x)
          
        right = mid - 1

      elif arr[mid] < x: # x must be located in second half
        left = mid + 1

      mid = (left + right) // 2

  if left <= right:
    return mid
  else:
    raise ValueError("Not found.")

class Customer:
  def __init__(self,my_id, name):
    self.customer_id = my_id
    self.name  = name 

  def __lt__(self, other):
    if not isinstance(other, Customer):
      raise TypeError(f"Cannot compare Customer to {type(other)}")
    return self.customer_id < other.customer_id 

  def __gt__(self, other):
    if not isinstance(other, Customer):
      raise TypeError(f"Cannot compare Customer to {type(other)}")
    return self.customer_id > other.customer_id  

  def __eq__(self, other):
    if not isinstance(other, Customer):
      return False
    return self.customer_id == other.customer_id  
  
  def __repr__(self):
    return f"<Customer {self.customer_id}, Name: {self.name}>"


c1 = Customer(1, "Mary")
c2 = Customer(2, "Bob")
c3 = Customer(3, "Charles")
c4 = Customer(5, "Anna")
c5 = Customer(8, "Maggie")

customers = [c5, c3, c2, c1, c4]
customers.sort()
#print(customers)
#print(c1)

#print(binary_search(customers, c4))

#li = [1,4,7,8,9,13,123,1262]
#li = ["aa","abc","abd","ac","ace","afg","bbb"]
#print(binary_search(li, "afg"))

x = 5
print(x.__lt__(30))





c1 = Customer(1, "Mary")
c5 = Customer(1, "Bob")
print(c1 == c5) # print(c1.__eq__(c5))
print(c1 is c5)
