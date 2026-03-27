class BrowserHistory:

  def __init__(self): 
    # there are different options for maintaining the data, including using a queue or a doubly linked list. 
    # Here, we will use two stacks, one containing previously visited websites, and one containing
    # websites available for forward navigation. 
    self.past = [] # the top of self.past is the current website
    self.future = [] 

  def visit(self, url):
    '''When the user visits a webpage with the given url, the method should 
       add the url to the end of the history and make it the current webpage.
    '''     
    self.past.append(url) # runs in O(1)
    self.future = []

  def back(self):
    '''Move one step back in the webpage history.
       This method returns the URL previous visited webpage, if there is one,
       and updates the current webpage.
       If there is no history, the method returns None
    '''
    if len(self.past) <= 1:
      return None
    self.future.append(self.past.pop()) # runs in O(1)
    return self.past[-1]

  def forward(self):
    '''Move one step forward in the webpage history
       Return the URL of the next visited webpage if there is one, i.e.,
       if the user (browser) previously performed the back action. If there
       is no webpage to navigate forward to, the method returns None.
    '''
    if len(self.future) == 0:
      return None
    self.past.append(self.future.pop()) # runs in O(1)
    return self.past[-1]

  def recently_visited(self):
    '''return a list of all recently visited webpages stored in the history.
    '''
    return self.past + self.future  # runs in O(n) -- concatenation assembles a new list.


if __name__ == "__main__":

  history = BrowserHistory()

  history.visit("columbia.edu")
  history.visit("netflix.com")
  history.visit("xkcd.com")
  print(history.back()) # prints "netflix.com"
  print(history.back()) # prints "columbia.edu"
  print(history.recently_visited()) # prints all three sites 
  print(history.forward()) # prints "netflix.com"
  history.visit("stackoverflow.com") 
  print(history.recently_visited()) # now xkcd.com is inaccessible 


