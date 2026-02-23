# COMS 2132 Intermediate Computing in Python 
## Homework 1, Spring 2026
### Due: Wednesday February 16, 11:59pm

**Submission:** All submissions must be through GitHub Classroom. Make sure to commit often and remember to push your final version to your remote repository on Github. We will grade the latest version you commit before the due date. 

Homework 1 has a programming part, and a written part. For the written part, please add all answers to the file written.md, either in plain text or using [Markdown formatting](https://www.markdownguide.org/basic-syntax/), which displays nicely in Github. 


### Part 1: Programming - Top-Down Program Design (60 pts)
In this part, you will implement a Python program that lets the user play a game of Wordle. If you
don’t know how to play Wordle, read [these instructions](https://www.nytimes.com/2023/08/01/crosswords/how-to-talk-about-wordle.html) or [play the game on the NY times website](https://www.nytimes.com/games/wordle/index.html).

Your goal is to design a program with a minimal user inte rface, that is, use simple text IO (input
and print functions) in the terminal. The interface of your program should look approximately like the following

<img src="https://raw.githubusercontent.com/cucs-python/public/refs/heads/main/w2132/lectures/figures/wordle_example_output.png">

In each step, your program obtains a guessed word from the user. The word must be exactly
five characters long and it must be one of the words in the dictionary. If the user enters a word
that is not in the dictionary, the program displays an error message (e.g., "Word not found!").
Unknown words DO NOT advance the game, i.e., the guess does not count. The program
should print a winning or losing message at the end.

You can use the Python package [colorama](https://pypi.org/project/colorama/) to output colorful text.
For example, a function to print one letter with green background could look like this:

```python
from colorama import Back
def print_green(letter):
    print(Back.GREEN + f" {letter} " + Back.RESET, end='')
```

Use the top-down design methodology shown in class (January 28 lecture) to
design and develop the program. Recall that top-down design (a.k.a. wishful programming)
consists of a sequence of (roughly) the following steps:

1. Write down the overall rules of the Wordle game
2. Design the main (top-level) function and its general structure
3. Break down the main function into individual functions solving sub-problems
4. Implement the function bodies
5. Complete and test the whole program
   
Requirement: Make at least five commits on the main / master branch that the TAs can view on your Github repository. 
There should be at least one Git commit roughly corresponding to each of the above steps. We will be looking for 
incremental progress roughly matching the top-down design strategy, not for any specific sequence of commits or commit messages.

**Hints**:
* Start by setting up your local Python development environment if you have not done so (If you need help setting up, visit OHs and/or the lab. We recommend the python.org python install, Visual Studio Code + git command line tools -- but any working setup/editor/IDE is fine)
* In ythe homework repository, write your program in a new file wordle.py, make sure to *add* it to the git repository. 
* The file wordle.txt is a plain text file containing potential Wordle words, one per line. Read in the list of words and select one at random.
* Use only the Python standard library and the colorama package.
* You can assume all user input is lower-case.
  
### Part 2: Written (40 pts)

#### 2.1) - 10 pts
Arrange the following functions in increasing order of their asymptotic growth rate. Indicate it two functions grow at the same rate. 

$N \log N$

$N!$

$128$

$\sqrt{N}$

$2^N$

$4^N$

$N^2$

$\log N$

$N^3$

$2^{N+1}$

$3N$

#### 2.2) - 8 pts
The rulers of an ancient kingdom demanded tribute payments from their vassals each year. The first year, they required 2 sacks of grain. Each subsequent year, the tribute was squared. The second year, the vassals had to pay 4 sacks of grain, then 16, then 256, then 65536, ...

* (a) What would the tribute be in year N?
* (b) How many years would it take for the annual tribute payment to reach D sacks of grain? 

Provide big-O answers. No justification is required.

#### 2.3)  - 6 pts
The number of operations executed by algorithm A is $8 N \log N$ and the number of operations executed by algorithm B is $2 N^2$. Determine $N_0$ such that A is better than B for $N \geq N_0$. Show your solution path.

#### 2.4) - 6 pts
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

#### 2.5) - 6 pts
As in 2.4, provide the running time of the following function in asymptotic (big-O) notation. Justify your answer. Recall that sorting is done in $O(N \log N)$

```python

def print_duplicates2(li):

  sorted_li = sorted(li)

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
 
#### 2.6) - 4 pts
Can you find a way to further improve the running of the function in 2.5? Provide Python code, the new running time, and provide a justification.
