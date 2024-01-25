# Spiral Matrix Generator Algorithm with Python

## Overview

The **Spiral Matrix Generator** algorithm creates a square matrix with a spiral pattern of numbers. It starts from the top left corner and spirals actions (right, down, left, up) filling in consecutive numbers inside the matrix.

## Usage

To apply a rule set, do the following:

1. Set the desired value of `n` (the dimensions of the rectangular matrix). The rule set requires `n` to be three or greater.

2. Execute the algorithm and it will generate a square matrix with a spiral pattern of numbers.

## Algorithm details

The ruleset uses a 2D listing ("frames") to symbolize a rectangular matrix. Initializes a counter (`current_number`) starting at -1 and iterates through the matrix, updating the factors based on the current direction (right, down, left, up).

The rule set reverses the course after completing a complete cycle in one course (right, down, left, up) and descales the matrix (`n`) after completing a right or left pass.

## Error handling

The ruleset contains errors that ensure that "n" should be 2 or more. If `n` is much less than 2, it prints an error message and now does not continue generating the matrix.

## Example

For `n = five` the ruleset generates the following matrix:

```py
    [
        [0, 1, 2, 3, 4],
        [15, 16, 17, 18, 5],
        [14, 23, 24, 19, 6],
        [13, 22, 21, 20, 7],
        [12, 11, 10, 9, 8],
    ]
```

## Notes

- The rule set assumes a square matrix as output.
- Adjust the value of `n` to generate matrices of extraordinary size.