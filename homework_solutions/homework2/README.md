# COMS 2132 Intermediate Computing in Python 
## Homework 2, Spring 2026
### Due: Friday March 13, 11:59pm

**Submission:** All submissions must be through GitHub Classroom. Make sure to commit often and remember to push your final version to your remote repository on Github. We will grade the latest version you commit before the due date. 

Homework 2 has a programming part, and a written part. For the written part, please add all answers to the file written.md, either in plain text or using [Markdown formatting](https://www.markdownguide.org/basic-syntax/), which displays nicely in Github. 


### Part 1: Programming (60 pts)

#### 1.1 Linked Lists (15 pts)

The file `linked_list.py` contains class definitions for a double linked list, essentially identical to the one we discussed in class. 

a) Implement the method `flip_pairs()` that flips each adjacent pair in the linked list. Note: if the list has an odd number of elements, the last element should remain in its original place. For example, if your original list is ["A" "B" "C" "D" "E"], after calling flip_pairs, the elements should be re-arranged to  ["B" "A" "D" "C" "E"]

The change to the list must be in-place by changing the prev and next references. You cannot simply assemble a new list.
Work out how the prev and next references have to be changed on paper, then implement the method. 

b) Recall the Iterator / Iterable protocol (see [Lecture 03 on Software Engineering/OOP fundamentals](https://github.com/coms2132-spring26/coms2132-spring26-materials/blob/main/lectures/lecture03/03-software-engineering.ipynb) ). We would like to be able to iterate over the elements in the list using a `for` loop so that the entire iteration only takes $O(N)$ time (as opposed to repeatedly calling `get(k)`, which is $O(N)$ for each call, and thus $O(N^2)$ for an entire iteration over the list). The linked_list.py code already implements an `__iter__` method, which returns an instance of class `LinkedListIterator`. Write the class `LinkedListIterator` so that you can iterate over the elements in the list using a `for` loop. You will have to implement both the `__init__` method and the `__next__` method. Recall that `__next__` should return one element at a time. When no more elements are available, the method should raise a `StopIteration` exception. 

c) Use ChatGPT or Columbia's CHAT to generate a number of test cases to verify that the flip\_pairs method and the LinkedListIterator work correctly. 
Include the test cases in the `main` section of the program and provide the prompts you used to generate them in a comment. Do the test-cases with your initial prompt capture all corner cases you can come up with? If not, how can you revise the prompt so that they do (provide both the original prompts and your revisions -- we want to see how you use the AI tools to work through the task of creating test cases).  


#### 1.2 Queues (15 pts)

The Counting Out game works like this: You have $n$ players and a fixed number $k$. 
The players stand in a circle. They are numbered from 1 to n. 
The players are counted proceeding in a clockwise direction. The first $k-1$ players are skipped. The $k$-th  player is "counted out" and leaves the circle. Then the next $k-1$ players are skipped, etc. 
The single player who remains in the end is the winner. 

In the file `counting_out.py`, write a Python program that reads integer n and k from the user and simulates this process using a queue. You can use a data structure from class, or the `dequeue` (double ended queue) from the [collections](https://docs.python.org/3/library/collections.html#collections.deque) module (recommended). 

The output of your program should look like this: 

```
What is n?9
What is k?4
1
2
3
4 is out.
5
6
7
8 is out.
9
1
2
3 is out.
5
6
7
9 is out.
1
2
5
6 is out.
7
1
2
5 is out.
7
1
2
7 is out.
1
2
1
2 is out.
1 wins.
```

#### 1.3 Browser History (15 pts)
The typical web browser maintains a history of visited web pages and allows the user to (1) view the history, (2) navigate back, and (3) navigate forward. The file `browser_history.py` contains a class `BrowserHistory` with empty method stubs for you to complete. The `BrowserHistory` keep track of the current webpage displayed, as well as a history of all previously visited webpages. Your task is to choose an appropriate data structure to store the URLs of visited webpages (which are just strings) and implement the methods. For each method, specify the running time in big-O notation (as a comment in the beginning of the method). 

The `BrowserHistory` should provide the following interface: 

```python
class BrowserHistory:

  def visit(self, url):
    '''When the user visits a webpage with the given url, the method should 
       add the url to the end of the history and make it the current webpage.
    '''     
    pass

  def back(self):
    '''Move one step back in the webpage history.
       This method returns the URL previous visited webpage, if there is one,
       and updates the current webpage.
       If there is no history, the method returns None
    '''
    pass

  def forward(self):
    '''Move one step forward in the webpage history
       Return the URL of the next visited webpage if there is one, i.e.,
       if the user (browser) previously performed the back action. If there
       is no webpage to navigate forward to, the method returns None.
    '''
    pass

  def recently_visited(self):
    '''return a list of all recently visited webpages stored in the history.
    '''
    pass
```

#### 1.4 Trees (15 pts)

The file `file_tree.py` contains definitions for a tree data structure representing files in a file system. 
Unlike in a regular tree, there are two different node classes, one for a `File` and one for a `Directory`. 
The `Directory` class contains a list of (arbitrarily many) children), which can be other Directories or Files.  A `File` does not contain any children. However, the `File` class has a data field for the `size` of the file. 

First, read through the `add_file` and `add_directory` method, which both rely on the `_find_directory` method. Understand how the `_find_directory` method traverses the tree in order to find the directory specified by a specific path name. 

a) In the method `print_tree` implement a way to display the tree. The output could look something like this (though other ways of printing the tree are acceptable, as long as the hierarchical structure is apparent from the output). It is recommended that you pass the "level" of the tree to the method and increment it with each function call, so you can print the correct indentation. 
```
+-/
  |
  +-hello.txt (100)
  |
  +-subdir
    |
    +-nested.txt (200)
    |
    +-another_subdir
      |
      +-world.txt (50)
    |
    +-nested.txt (150)
```

b) The method `total_size_recursive(self, node)` should implement a recursive traversal of the tree starting at `node` and return the sum of all file sizes in the tree (500 in the example, when called for the root node). Hint: recursively compute the size of each subtree of node, sum these sizes together, and return the total. 

c) If we need to compute the sum of file sizes frequently, performing a full recursive traversal each time is expensive. Instead, modify the code so that each `Directory` keeps track of the total size of all files in this directory (or any subdirectory). These totals should be updated whenever a new file is inserted. Modify the `add_file` method to update the totals when a new file is inserted. You may want to rewrite the `_find_directory` method or write your own code for finding the insertion site (as part of the `add_file` implementation). In the `__main__` section include code to test that functionality.
  
### Part 2: Written (40 pts)

#### 2.1) - List (5 pts)
Describe how to implement the `reverse()` operation on a double linked list in O(1)? Reverse should logically reverse the order of the elements in the list.

#### 2.2) - Stacks and Queues (10 pts)

a) Assume you are given an input queue q containing ['M','E','L','O','N','S'] (with 'M' being the entry at the front of the queue). Your goal is to convert is to rearrange the elements into a new list li in the following order: ['L','E','M','O','N','S']. You may only use a single stack s as temporary storage. Provide a sequence of dequeue, push, pop, and append operations. 

b) Explain why you cannot rearrange ['D','E','S','P','A','I','R'] into  ['P','R','A','I','S','E,'D'] using a single stack. 

#### 2.3) - Tree Traversals (10 pts)
Assume that you are given both the preorder and postorder traversal of some binary tree $t$. Prove that this information, taken together, is not necessarily sufficient to reconstruct $t$ uniquely (this is true even if each value in $t$ appears only once). Hint: Show two different trees that have an identical preorder and postorder traversal sequence. 

#### 2.4) - Binary Search Trees (15 pts)
A binary search tree (BST) is a binary tree with the following property (BST property). For each node with value $v$ all nodes in the left subtree (the subtree rooted in the left child) have values $u < v$, and all nodes in the right subtree (the subtree rooted in the right child) have values $w > v$.

a) To insert a new value $x$ into the tree, we start at the root node. If $x$ is less than the value of that node, we continue comparing $x$ with the left child. If $x$ is greater than the value of the node, we continue comparing $x$ with the right child. We proceed with these comparisons, moving down the tree until one of the following conditions applies. If we find a node a node with value identical to $x$, the value is already in the tree and we do nothing. 
If we are at node $n$ and need to move left (i.e. $x$ is less than the value of $n) and there is no further left child, we insert a new node with value $x$ as the new left child below $n$. Similary, if we are at node $n$ and need to move right and there is no further right child, we insert a new node with value $x$ as the right child below $n$. 

Show the result of inserting the values 4,2,1,6,3,5 into an initially empty binary search tree. 

b) What is the best case and worst case running time (number of comparisons) for the insert operation in big-O notation? Construct an example for the worst case. 

c) We can use a Binary Search Tree to sort a set of values (note there cannot be any duplicates in the tree, so this is not a general-purpose sorting algorithm). We first insert the values into the BST one-by-one. Then we perform an in-order traversal to produce the values in sorted order. Provide the best case and worst case running time for this sorting algorithm applied to $N$ elements in big-O notation.


