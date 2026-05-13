# COMS 2132 Intermediate Computing in Python 
## Homework 3, Spring 2026
### Due: Thursday April 30, 11:59pm 

**Submission:** All submissions must be through GitHub Classroom. Make sure to commit often and remember to push your final version to your remote repository on Github. We will grade the latest version you commit before the due date. 

### Part 2: Written (45 pts)

#### 2.1) - Hash Tables (15 pts) 

Insert the following keys one-by-one into an initially empty hash table of size 7. Use the hash code function $f(x) = x$ and the compression function $g(x) = x mod 7$.

10, 1, 18, 15, 26, 11, 19

Show the result for
 
* (a) a separate chaining hash table (you do not have to worry about the load factor -- no need to rehash).


[0]: 
[1]: 1,15
[2]: 
[3]: 10
[4]: 18,11
[5]: 26,19
[6]: 


* (b) an open addressing hash table using linear probing. 

[0]: 19
[1]: 1
[2]: 15
[3]: 10
[4]: 18
[5]: 26
[6]: 11

#### 2.2) - Heaps (15 pts)

* (a) Insert the values 8, 12, 14, 11, 9, 16, 10, 7, 6 into an initially empty binary min-heap. Show the heap after each insertion as an array or as a tree. You do not need to show each individual percolation step.

insert 8:    [8]
insert 12:   [8, 12]
insert 14:   [8, 12, 14]
insert 11:   [8, 11, 14, 12]
insert 9:    [8, 9, 14, 12, 11]
insert 16:   [8, 9, 14, 12, 11, 16]
insert 10:   [8, 9, 10, 12, 11, 16, 14]
insert 7:    [7, 8, 10, 9, 11, 16, 14, 12]
insert 6:    [6, 7, 10, 8, 11, 16, 14, 12, 9]

Or as a tree: 
```
                 6
              /      \
             7       10
           /   \   /    \
          8    11 16    14
         / \
        12  9

```

* (b) Perform three `delete_min` operations on the final heap from part (a). Show the heap after each `delete_min` as a tree or array.

delete_min -> 6: [7, 8, 10, 9, 11, 16, 14, 12]
delete_min -> 7: [8, 9, 10, 12, 11, 16, 14]
delete_min -> 8: [9, 11, 10, 12, 14, 16]

Or the final heap as a tree: 

```
                 9
              /      \
             11      10
           /   \   /    
          12   14 16    
```



#### 2.3) - Sorting (15 pts)

Consider the input array `[3, 5, 2, 6, 4, 7, 1]`. 
Show how each of the following sorting algorithms would sort the array. 

* (a) Selection Sort (show the array after each selection step, i.e. after each iteration of the outer loop, including the position of the p index) 

 p=0
[3, 5, 2, 6, 4, 7, 1]  initial array

    p=1
[1, 5, 2, 6, 4, 7, 3] 

       p=2
[1, 2, 5, 6, 4, 7, 3] 

          p=3
[1, 2, 3, 6, 4, 7, 5]

             p=4
[1, 2, 3, 4, 6, 7, 5]

                p=5
[1, 2, 3, 4, 5, 7, 6] 

                   p=6
[1, 2, 3, 4, 5, 6, 7] 


* (b) Insertion Sort  (show the array after each insertion step, including the position of the p index) 

    p=1
[3, 5, 2, 6, 4, 7, 1]  initial array
                 
       p=2
[3, 5, 2, 6, 4, 7, 1] 

                  
          p=3
[2, 3, 5, 6, 4, 7, 1] 

             p=4
[2, 3, 5, 6, 4, 7, 1]  
                          
                p=5
[2, 3, 4, 5, 6, 7, 1]  

                   p=6    
[2, 3, 4, 5, 6, 7, 1] 

                            
final 
[1, 2, 3, 4, 5, 6, 7] 

* (c) Merge Sort (you do not have to show the individual merge steps)

```
                [3, 5, 2, 6, 4, 7, 1]
              /                       \
        [3, 5, 2]                  [6, 4, 7, 1]
      /        \                  /           \
    [3]      [5, 2]            [6, 4]        [7, 1]
     \       /   \              /   \         /   \
      \    [5]   [2]          [6]   [4]     [7]   [1]
       \     \   /              \   /         \   /
        \   [2, 5]             [4, 6]        [1, 7]
         \    /                    \           /
       [2, 3, 5]                  [1, 4, 6, 7]
              \                   /
             [1, 2, 3, 4, 5, 6, 7]

```

