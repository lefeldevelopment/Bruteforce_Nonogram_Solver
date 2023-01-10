# Bruteforce_Nonogram_Solver
A Nonogram, also known as a Picture Cross or Griddlers, is a puzzle that consists of a blank grid with clues along the sides of the grid. The goal is to fill in the grid according to the clues, revealing a hidden image. This Nonogram Solver is a python class that is capable of solving such puzzles by using a backtracking algorithm.

## Getting Started
The solver requires two inputs: the size of the grid and the clues for each row and column. The size of the grid is given as a tuple of the form (height, width). The clues for each row and column are given as a list of lists, where each sub-list contains the clues for a single row or column.

## Prerequisites
This solver is written in Python and uses the itertools library. Make sure that these are installed on your system.

## Usage
You can use the Nonogram Solver in two ways:

1. Using Input: You can create an instance of the class by calling the from_input() class method. This method will prompt the user to enter the size and clues through the command line.

```py
  nonogram_solve = Nonogram_solver.from_input()
  nonogram_solve.solve()
```

2. Using Variables: You can create an instance of the class by passing the size and clues as arguments to the constructor.

```py
  size = (5, 5)
  preset = (
      [[3],[2],[1,1],[1,1],[1]],
      [[1,],[4],[2,1],[2],[]]
  )

  nonogram_solve = Nonogram_solver(size, preset)
  nonogram_solve = solver.solve()
```

When printed, the ``Nonogram_solver`` Object prints out a matix of the field:

```py
>>> print(nonogram_solve)
■ ■ ■ x x
x ■ ■ x x
x ■ x ■ x
x ■ x ■ x
x x ■ x x
```
