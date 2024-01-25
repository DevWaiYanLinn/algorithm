# Spiral Matrix Generator Algorithm with Python

## Overview

The **Spiral Matrix Generator** algorithm creates a square matrix with a spiral pattern of numbers. It starts from the top-left corner and moves in a spiral direction (right, down, left, top), filling in the matrix with consecutive numbers.

## Usage

To use the algorithm, follow these steps:

1. Set the desired value of `n` (the size of the square matrix). The algorithm requires `n` to be 3 or greater.

2. Execute the algorithm, and it will generate a square matrix with a spiral pattern of numbers.

## Algorithm Details

The algorithm uses a 2D list (`frames`) to represent the square matrix. It initializes a counter (`current_number`) starting from -1 and iterates through the matrix, updating elements based on the current direction (right, down, left, top).

The algorithm rotates the direction after completing a full cycle in one direction (right, down, left, top), and it reduces the size of the matrix (`n`) after completing either right or left traversal.

## Error Handling

The algorithm includes error handling to ensure that `n` must be 2 or greater. If `n` is less than 2, it prints an error message and does not proceed with matrix generation.

## Example

For `n = 5`, the algorithm generates the following matrix:

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

- The algorithm assumes a square matrix as output.
- Adjust the value of `n` to generate different-sized matrices.

