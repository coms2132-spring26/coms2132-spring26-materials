# COMS 2132 Intermediate Computing in Python 
## Homework 2, Spring 2026
### Written Solution 

#### 2.1) - List (5 pts)
> Describe how to implement the `reverse()` operation on a double linked list in O(1)? Reverse should logically reverse the order of the elements in the list.

We simply add a boolean data field to the list class, such as `self.is_reversed=False`. The reverse() method simply negates/flips that boolean. Then, all other list methods needs to be updated. If `self.is_reversed == True` all methods moving through the list (indexing, inserting, removing, printing, searching) must start at the trailed node and follow the prev references until the header is reached. 

#### 2.2) - Stacks and Queues (10 pts)

> a) Assume you are given an input queue q containing ['M','E','L','O','N','S'] (with 'M' being the entry at the front of the queue). Your goal is to convert is to rearrange the elements into a new list li in the following order: ['L','E','M','O','N','S']. You may only use a single stack s as temporary storage. Provide a sequence of dequeue, push, pop, and append operations. 

```
s.push(q.dequeue()) # push(M)
s.push(q.dequeue()) # push(E)
s.push(q.dequeue()) # push(L)
s.pop() # -> L
s.pop() # -> E
s.pop() # -> M
s.push(q.dequeue()) # push(O)
s.pop() # -> O
s.push(q.dequeue()) # push(N)
s.pop() # -> N
s.push(q.dequeue()) # push(S)
s.pop() # -> S

```

> b) Explain why you cannot rearrange ['D','E','S','P','A','I','R','] into  ['P','R','A','I','S','E,'D'] using a single stack. 

```
push(D)
push(E)
push(S)
push(P)
pop() # -> P. At this point we need to push A and I to get to the R as the next letter
push(A)
push(I)
push(R)
pop() # -> R. 
Now we would have to get the A next, but the letter on top of the stack is I.
```

#### 2.3) - Tree Traversals (10 pts)
> Assume that you are given both the preorder and postorder traversal of some binary tree $t$. Prove that this information, taken together, is not necessarily sufficient to reconstruct $t$ uniquely (this is true even if each value in $t$ appears only once). Hint: Show two different trees that have an identical preorder and postorder traversal sequence. 

```
Tree 1: 

        A
       /
      B
     /
    C

Preorder: A B C
Postorder: C B A

Tree 2: 

       A
      /
     B
      \
       C

Preorder: A B C
Postorder: C B A
```

The two trees are different, yet their pre and postorder traversal sequences are the same. 

#### 2.4) - Binary Search Trees (15 pts)
> A binary search tree (BST) is a binary tree with the following property (BST property). For each node with value $v$ all nodes in the left subtree (the subtree rooted in the left child) have values $u < v$, and all nodes in the right subtree (the subtree rooted in the right child) have values $w > v$.
>
> a) To insert a new value $x$ into the tree, we start at the root node. If $x$ is less than the value of that node, we continue comparing $x$ with the left child. If $x$ is greater than the value of the node, we continue comparing $x$ with the right child. We proceed with these comparisons, moving down the tree until one of the following conditions applies. If we find a node a node with value identical to $x$, the value is already in the tree and we do nothing. 
> If we are at node $n$ and need to move left (i.e. $x$ is less than the value of $n) and there is no further left child, we insert a new node with value $x$ as the new left child below $n$. Similary, if we are at node $n$ and need to move right and there is no further right child, we insert a new node with value $x$ as the right child below $n$. 
>
> Show the result of inserting the values 4,2,1,6,3,5 into an initially empty binary search tree. 

```

              4
            /   \
           2     6 
          / \   / 
         1   3 5


```

> b) What is the best case and worst case running time (number of comparisons) for the insert operation in big-O notation? Construct an example for the worst case. 



Insertion requires to decent from the root to a leaf, so the running time depends on the height of the tree. 

Best case: $O(\log N)$ if the tree is *complete* (all levels have the max number of nodes). Then its height is $O(\log N)$.

Worst case: $O(N)$ -- if the tree is completely unbalanced (i.e. just a chain of nodes with a single child) it has a height of $O(N)$.

```
   1
    \
     2
      \
       3
        \ 
         4
          \
           5
            \
             6               
```
                

>c) We can use a Binary Search Tree to sort a set of values (note there cannot be any duplicates in the tree, so this is not a general-purpose sorting algorithm). We first insert the values into the BST one-by-one. Then we perform an in-order traversal to produce the values in sorted order. Provide the best case and worst case running time for this sorting algorithm applied to $N$ elements in big-O notation.

The traversal will always take $O(N)$. In the best case (tree is always close to complete), each of the $N$ inserts takes $O(\log N)$ time resulting in $N \cdot  O(\log N) + O(N) = O(N \log N)$


