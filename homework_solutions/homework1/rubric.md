# 2132 Spring 26 - Homework 1 Rubric

## Part 1 - Top-Down Program Design (60 pts)

30 pts - at least 5 commits each with some incremental progress
* 4 pts for every missing commit or for every commit that does not show progress
* 15 pts if submitted jupyter notebook instead of .py

15 pts - the code follows top-down design: subproblems are solved in individual functions
* 10 pts if the whole game is implemented in a single function

15 pts - correct game logic:

* 4 pts - Asks for user input repeatedly until 6 incorrect guesses are reached or user
guesses the word correctly

* 4 pts - Checks that the input word is valid (5 characters long, in the dictionary) and
handles invalid words without causing exceptions

* 4 pts - Colors the letters in guessed words correctly (ignore the issue with double letters 
    	in the guess)

* 3 pts - Displays winning/losing message
* 1 point deduction if one of the messages are missing
		
10 point deduction for not commenting out their secret word

2 point deduction if game works but error on lines that’s not related to the game logic	

-30 Points if code does not run correctly
-10 points if you need to modify their code

## Part 2 - Written (40 pts)
2.1  10 pts
* -1 for each function that has the wrong place in the order
* -2 for not recognizing that 2^N = Theta(2^{N+1})
* -3 if the order is “correct”, but they flipped the greater signs to less than signs or vice versa

2.2  8 pts
* 4 pts,    -2 if partially correct
* 4 pts,    -2 if partially correct or result not in big-O

2.3 6 pts
* 3 pts for the solution 
* 3 pts for providing reasonable justification (either calculation or a graph)
* -3 if they use the wrong base

2.4 6 pts
* 3 pts for correct running time
* 3 pts for reasonable justification

2.5 6 pts
* 3 pts for correct running time
 * -1pt for not condensing the runtime
* 3 pts for reasonable justification 

2.6 4 pts
* 2 pts for solution better than N^2
* 1 pt correct runtime analysis
* 1 pt analysis for runtime analysis

