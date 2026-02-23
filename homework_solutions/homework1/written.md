# COMS 2132 Homework 1 -- Written Portion
## Written Solution

### 2.1

* $128$  (constant, O(1) )
* $log N$ (logarithmic)
* $\sqrt{n}$  (note $\sqrt{n} = N^{1/2}$)
* $3N$ (linear, O(N) )
* $N log N$
* $N^2$ (quadratic) 
* $N^3$ (cubic) 
* $2^N$ and $2^{N+1}$ (exponential, note $2^{N+1} = 2\cdot 2^{N} = O(2^N)$) 
* $4^N$ 
* $N!$

### 2.2

The rulers of an ancient kingdom demanded tribute payments from their vassals each year. The first year, they required 2 sacks of grain. Each subsequent year, the tribute was squared. The second year, the vassals had to pay 4 sacks of grain, then 16, then 256, then 65536, ...

* (a) What would the tribute be in year N?

$$D = 2^(2^{(N-1)})$

* (b) 
solve the equation in (a) for $N$. 

$N - 1 = \log_2 \log_2 D$
Thus
$N =  O( \log \log D)$

### 2.3
The number of operations executed by algorithm A is $8 N \log N$ and the number of operations executed by algorithm B is $2 N^2$. Determine $N_0$ such that A is better than B for $N \geq N_0$. Show your solution path.


$$8N \log_2 N \leq 2 N^2$$
$$4 N\log_2 N \leq  N^2$$ 
$$4 \log_2 N \leq N$$ 
$$\log_2 N \leq \frac{N}{4}$$

Solving equations of this type is tricky, in general. But here we can use our intuition to find the solution, which is $N_0 = 16$. On the left hand side, we are looking for a power of 2. From the right hand side, we know the solution is a multiple of 4. 

$$(\log_2 4  = 2) \geq \frac{2}{4}$$
$$(\log_2 8  = 3) \geq \frac{8}{4}$$
$$(\log_2 16  = 4) = \frac{16}{4}$$



### 2.4
The following function prints all duplicates in a list of $N$ items. Provide the running time of this function in asymptotic (big-O) notation. Justify your answer.
You can assume that list accesses such as $li[i]$ are $O(1)$, i.e. constant time. The append method is also $O(1)$.

```python

def print_duplicates(li):

  duplicates = []

  for i in range(len(li)):
    for j in range(i+1, len(li)):
      if li[i] == li[j]:

      seen = False
      for k in range(len(duplicates)):
        if duplicates[k] == li[i]:
          seen = True
      if not seen:
        duplicates.append(li[i])
        print(li[i])
```


The outer two loops for i and j each run in $O(N)$. The runtime for nested loops must be multiplied, so we get $O(N^2)$. In the worst case, half the elements in li are duplicates (i.e. something like [1,1,2,2,3,3,...], so the duplicates list might become $O(N)$ in length. Searching through that list (the innermost nested loop for k) also takes $O(N)$, resulting in a total of $O(N^3)$.

### 2.5)
As in 2.4, provide the running time of the following function in asymptotic (big-O) notation. Justify your answer. Recall that sorting is done in $O(N \log N)$

```python

def print_duplicates2(li):

  li = sorted(li)

  duplicates = []

  for i in range(1,len(li)):
    if li[i] == li[i-1]:

      seen = False
      for k in range(len(duplicates)):
        if duplicates[k] == li[i]:
          seen = True
      if not seen:
        duplicates.append(li[i])
        print(li[i])
```
Sorting the list takes $O(N log N)$. The loop over i takes $O(N)$. The nested loop for the duplicate check also takes $O(N)$ in the worst case. So we get $O(N log N) + O(N^2) = O(N^2)$ 

 
### 2.6)
Can you find a way to further improve the running of the function in 2.5? Provide Python code, the new running time, and provide a justification.

A simple optimization uses the fact that all duplicates are adjacent to each other in the sorted list. The trick is to skip any additional duplicates to avoid printing them multiple times. 

```python

def print_duplicates3(li):

  li = sorted(li)

  i = 1
  while i < len(li):
    if li[i] == li[i-1]:  # found a duplicate
      print(li[i])

      # skip all other copies of the duplicate
      while i < len(li)-1 and  li[i] == li[i+1]:
        i += 1
      
    i += 1
```

The total time required for the two while loops is only $O(N)$ because the i index just moves through the list once, left to right. 
Now the time for sorting dominates. We get $O(N log N) + O(N) = O(N log N)$.


An alternative is to use a set, which has expected $O(1)$ operations (adding and membership checking). The algorihtm would run in expected $O(N)$ time. 

```python
def print_duplicates4(li): 

  seen = set()
  duplicates = set()
  for i in li: 
    if li[i] in seen(): 
      if not li[i] in duplicates: 
        duplicates.add(li[i])
        print(li[i])
    seen.add(li[i]) 
```
