# Zebra Logic Puzzle Solver

This project is designed to solve a logic puzzle involving attributes of 4 boys (`shirts`, `names`, `movies`, `snacks`, `ages`).
The object is to place each attribute in the correct order based on clues.
This project uses Python and Prolog to solve the puzzle.

## Logic Puzzle
Attributes: `shirts`, `names`, `movies`, `snacks`, `ages`\
Boys: `Boy 1`, `Boy 2`, `Boy 3`, `Boy 4`\
Clues:
- Joshua is at one of the ends.
- The boy wearing the Black shirt is somewhere to the left of the youngest boy.
- Joshua likes Horror movies.
- The 14-year-old boy is at the third position.
- The boy wearing the Red shirt is somewhere between the 13-year-old boy and the one who likes Action movies, in that order.
- Daniel likes Thriller movies.
- The boy who is going to eat Cookies is at one of the ends.
- The boy wearing the Black shirt is exactly to the left of the one who likes Thriller movies.
- The boy who is going to eat Crackers is exactly to the right of the boy who likes Comedy movies.
- The boy wearing the Red shirt is somewhere between the boy who is going to eat Popcorn and Nicholas, in that order.
- At one of the ends is the boy who likes Thriller movies.
- Nicholas is somewhere between Joshua and Daniel, in that order.
- Nicholas is somewhere between Joshua and Daniel, in that order.

## Files
- `main.py`: Python file that solves the logic puzzle
- `Prolog.py` : Prolog file that solves the logic puzzle

## Python
### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python code.
3. Run the program with the command:
   ```
   python main.py
   ```
### Output
```
Solution:
Boy 1: Name=Daniel, Age=12, Shirt=Green, Movie=Action, Snack=Chips
Boy 2: Name=Joshua, Age=13, Shirt=Blue, Movie=Horror, Snack=Popcorn
Boy 3: Name=Nicholas, Age=14, Shirt=Red, Movie=Thriller, Snack=Cookies
Boy 4: Name=Ryan, Age=11, Shirt=Black, Movie=Comedy, Snack=Crackers
```
## Prolog
### Running the Program
1. Open a prolog compiler (Swish.swi)
2. Copy the code given and paste into compiler
3. Run the program with an output command : print_solution.
   ```
   Prolog Prolog.py
   ```
### Output
Boy 1: [name:joshua, age:12, shirt:green, movie:horror, snack:popcorn]
Boy 2: [name:ryan, age:13, shirt:red, movie:comedy, snack:chips]
Boy 3: [name:nicholas, age:14, shirt:black, movie:action, snack:crackers]
Boy 4: [name:daniel, age:11, shirt:blue, movie:thriller, snack:cookies]
   
