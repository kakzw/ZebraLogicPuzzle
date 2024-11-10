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
- `swish.pl` : Prolog file that solves the logic puzzle

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
Boy 1: Shirt=Green, Name=Joshua, Movie=Horror, Snack=Popcorn, Age=13
Boy 2: Shirt=Red, Name=Ryan, Movie=Comedy, Snack=Chips, Age=12
Boy 3: Shirt=Black, Name=Nicholas, Movie=Action, Snack=Crackers, Age=14
Boy 4: Shirt=Blue, Name=Daniel, Movie=Thriller, Snack=Cookies, Age=11
```
## Prolog
### Running the Program
1. Open a prolog compiler (Swish.swi)
2. Copy the code given in `swish.pl` and paste into compiler
3. Run the program with an output command: .
   ```
   print_solution
   ```
### Output
```
Solution:
[boy1:shirt:green, name:joshua, movie:horror, snack:popcorn, age:13]
[boy2:shirt:red, name:ryan, movie:comedy, snack:chips, age:12]
[boy3:shirt:black, name:nicholas, movie:action, snack:crackers, age:14]
[boy4:shirt:blue, name:daniel, movie:thriller, snack:cookies, age:11]
```
