# COMS 2132 Intermediate Computing in Python 
## Homework 3, Spring 2026
### Due: Thursday April 30, 11:59pm 

**Submission:** All submissions must be through GitHub Classroom. Make sure to commit often and remember to push your final version to your remote repository on Github. We will grade the latest version you commit before the due date. 

Homework 3 has a programming part, and a written part. For the written part, please add all answers to the file written.md, either in plain text or using [Markdown formatting](https://www.markdownguide.org/basic-syntax/), which displays nicely in Github. 


### Part 1: Programming (55 pts)


#### 1.1) k-best Counter (15 pts)
Assume you are given a sequence of values (for example, measurements obtained from a sensor or from a web API, see problem 1.2). Only one value is provided at a time. We do not know how many elements there are in the sequence. In fact, there could be infinitely many. This is also called a *stream* of values. The goal is to be able to retrieve the k-largest elements seen so far at any time.

**TODO:** In the file `kbest.py`, complete the class KBestCounter that keeps track of the $k$-largest elements seen so far in a stream of data using a priority queue / heap. The class should have two methods:

* `def count(self, x)` - process the next element in the set of data. 
* `def kbest(self)` - return a list of the $k$-largest elements that were ever passed to the `count` method. The result does not have to be in a particular order. 

Important: `KBestCounter` objects should only store the $k$-largest items. Other items should not be stored. 

You can use the heap class discussed in class, or you can use the [heapq module](https://docs.python.org/3/library/heapq.html).

The function `test_k_best` generates 100 random numbers and presents each to the KBestCounter. After each 10 numbers, it calls the `kbest` method and prints the 5 largest numbers seen so far. 

#### 1.2) Earthquake Monitor (20 pts) 
(part b of this problem uses the k-best counter class from problem 1.2)

The US Geological Servey (USGS) provides a real-time data feed of seismic events through their [API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).

The data is available in various formats, but here we will use their [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON) API. The API returns the full list of earthquake events over the last hour, and the data is updated every minute. 

Take a look at the file `earthquakes.py`. 
The class `Earthquake` represents a single earthquake event, including the time, magnitude (as a float), place (as a plain-text string), longitude, latitude, and depth. Time is represented as the number of seconds since epoch (Jan 1 1970, 00:00:00).

The function `fetch_earthquake_data` accesses the USGS feed and returns a list of `Earthquake` instances. 
The main program currently fetches the raw earthquake data every 60 seconds, and then prints *all* earthquaes returned in the data stream. 

```bash 
$ python earthquakes.py
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA

2025-03-28 11:29:15.670000 -- 1.06 3 km NE of The Geysers, CA
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA
```

**TODO**

* a) write the method `print_new_quakes`, which should repeatedly fetch the API data every 60 seconds, but only print _new_ earthquakes in each iteration (if any). The output should be something like this: 

```$ python earthquakes.py
2025-03-28 11:06:19.780000 -- 0.97 10 km SSE of Pinnacles, CA
2025-03-28 11:03:17.670000 -- 0.93 8 km NNW of The Geysers, CA
2025-03-28 10:54:47.360000 -- 0.71 7 km WNW of Cobb, CA
2025-03-28 10:38:07.220000 -- 2.12 13 km SSE of Volcano, Hawaii
2025-03-28 10:34:20.770000 -- 1.49 9 km NW of The Geysers, CA

2025-03-28 11:29:15.670000 -- 1.06 3 km NE of The Geysers, CA
```

You will need to keep track of the earthquakes seen so far in a python `set`. Sets (in Python and other languages) are hashtables that store only keys. Add an appropriate `__hash__(self)` method and `__eq__(self)` method to the `Earthquake` class to ensure that duplicates are detected correctly. 

* b) write the method `print_k_largest(k)`, which should repeatedly fetch the API data every 60 seconds and then print the $k$-largest earthquakes seen in the data stream so far. You can use the k-best counter from problem 1.1 (using `from kbest import KBestCounter`).
You will still need to use a `set` for duplicate detection. 
In order to use the k-best counter, you will need to make your `Earthquake` class comparable by magnitude by implementing appropriate ``_gt__`, ``__lt__``, and ``__eq__`` methods.

#### 1.3) Lights-Out (20 pts) 

Lights-out is a simple puzzle game. We will play the 4x4 version. 

The game is played on a grid, of "lights", that is each square either has value 0 (light off) or value 1 (light on). 

```
+-+-+-+-+
|0|1|0|0|
+-+-+-+-+
|1|0|1|0|
+-+-+-+-+
|0|1|0|1|
+-+-+-+-+
|0|0|1|0|
+-+-+-+-+
```

A specific configuration on the grid is called a state. A move in the game involves flipping/toggling one of the lights, from on(1) to off(0), or off(0) to on(1). But toggling a specific light will also toggle all of its immediate neighbors (left, right, up, down, if that position exists). 
For example, turning on the light in row 1, column 1 would result in

```
+-+-+-+-+
|0|0|0|0|
+-+-+-+-+
|0|1|0|0|
+-+-+-+-+
|0|0|0|1|
+-+-+-+-+
|0|0|1|0|
+-+-+-+-+
```

The goal of the game is to turn all lights off.

**State Transition System**

The file `lights_out.py` contains code to represent the lights out game as a state transition system. Each state is represented as a tuple of tuples. For example, the initial state above is represented as 

```
s= 
((0,1,0,0),  
 (1,0,1,0),  
 (0,1,0,1),  
 (0,0,1,0))
```

The function `toggle(state, row, col)` toggles a light and returns a new state. Calling `toggle(s, 1,1)` will return 

```
((0,0,0,0),  
 (0,1,0,0),  
 (0,0,0,1),  
 (0,0,1,0))
```

The function `goal_test(state)` returns True if all lights are off, i.e. all values in the state are 0. 

(a) **TODO**: Write the function `solve(start_state)` that will ultimately return a list of (row,column) tuples that turn off all lights. 

The function should use Breadth First Search to attempt to find the shortest solution so the game. Recall that BFS works like this: 
Keep a todo list of states on a Queue (you can use `collections.dequeu`), initially store the start state. As long as the queue is not empty, dequeu the next state ("visit"). Call the `toggle` function on each state to get all successors ("discover"). Add all the successors back to the queue. 

You need to ensure that each state is "discovered" only once. Also, because you ultimately need to retrace your steps to find the solution, you should record which (row,column) was switched on to get to each state and what the predecessor state was. I recommend you create two dictionaries `move` and `predecessor`. For example, turning on (1,1) in initial state above, should add the following entries to the dictionaries. 

`predecessor[((0,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0))] = ((0,1,0,0),(1,0,1,0),(0,1,0,1),(0,0,1,0))`

and 

`move[((0,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0))] = (1,1)`.


Once the BFS loop finishes, you can use the two dictionaries to retrace your steps to find the shortest path solution. Return a list of tuples. Note, that some start states are not solvable, in which case your function should return None. 

(b) **TODO**: Use generative AI (ChatGPT or similar) to add a tkInter based graphical user interface (GUI), using your code as a starting point. The GUI should show the game board for the start state and then let the user play the game. The GUI should contain a "solve" button, that will solve the game starting at the current state on the board. Solving the game should animate the individual moves required (i.e. show them step by step with a slight pause after each). Tinker with the prompt to make the GUI look visually apealing. Provide your initial prompt and any revisions as a comment in your code.



### Part 2: Written (45 pts)

#### 2.1) - Hash Tables (15 pts) 

Insert the following keys one-by-one into an initially empty hash table of size 7. Use the hash code function $f(x) = x$ and the compression function $g(x) = x mod 7$.

10, 1, 18, 15, 26, 11, 19

Show the result for
 
* (a) a separate chaining hash table (you do not have to worry about the load factor -- no need to rehash).
* (b) an open addressing hash table using linear probing. 

#### 2.2) - Heaps (15 pts)

* (a) Insert the values 8, 12, 14, 11, 9, 16, 10, 7, 6 into an initially empty binary min-heap. Show the heap after each insertion as an array or as a tree. You do not need to show each individual percolation step.

* (b) Perform three `delete_min` operations on the final heap from part (a). Show the heap after each `delete_min` as a tree or array.

#### 2.3) - Sorting (15 pts)

Consider the input array `[3, 5, 2, 6, 4, 7, 1]`. 
Show how each of the following sorting algorithms would sort the array. 

* (a) Selection Sort (show the array after each selection step, i.e. after each iteration of the outer loop, including the position of the p index) 
* (b) Insertion Sort  (show the array after each insertion step, including the position of the p index) 
* (c) Merge Sort (you do not have to show the individual merge steps)

