import heapq # recommended, but you can also use the heap implementation discussed in class
import random # for testing

class KBestCounter:

  def __init__(self,k):
    self.k = k
    self.heap = []


  def count(self, x): 
    """process the next element in the set of data."""
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, x)
      return
      
    if x > self.heap[0]: # x should be part of the k-largest
        heapq.heappop(self.heap)
        heapq.heappush(self.heap, x)
  

  def kbest(self): 
    """return a list of the $k$-largest elements that were ever passed to the `count` method."""
    return self.heap


def test_k_best():

  counter = KBestCounter(5)

  for i in range(1,101):
    next_value = random.randint(1,1000)
    counter.count(next_value)
    if i % 10 == 0:
      print(f"Current k-largest: {counter.kbest()}")
      

if __name__ == "__main__":

  test_k_best()
  
