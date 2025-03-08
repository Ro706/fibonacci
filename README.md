# Fibonacci Number Calculator

This is a simple Python program that calculates the nth Fibonacci number using a recursive function. The program prompts the user to input a non-negative integer and then computes the corresponding Fibonacci number.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Acknowledgements](#acknowledgements)

## Features

- Computes the nth Fibonacci number.
- Validates user input to ensure it is a non-negative integer.
- Provides error messages for incorrect inputs.

## Requirements

- Python 3.12.9 or later.

## Usage

1. **Clone the repository** or **download the script** to your local machine.
2. **Open a terminal or command prompt** and navigate to the directory containing the script.
3. **Run the script** using the following command:
   ```sh
   python fibonacci.py
   ```

### Example

```sh
~$ python fibonacci.py
Enter a non-negative integer: 10
55
```

## Code Explanation

### Fibonacci Function

```python
def Fibonacci(n):
    """
    Function to return the nth Fibonacci number.
    """
    if n < 0:
        return "Incorrect input"  # Handle negative input

    # Base cases
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        # Recursive case
        return Fibonacci(n - 1) + Fibonacci(n - 2)
```

- **Input Handling**: The function checks if `n` is a negative number and returns an error message if so.
- **Base Cases**: If `n` is 0 or 1, the function returns 0 or 1 respectively.
- **Recursive Case**: For other values, the function recursively calculates the Fibonacci number.

### Driver Program

```python
# Driver Program
try:
    n = int(input("Enter a non-negative integer: "))
    print(Fibonacci(n))
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
```

- **Input Prompt**: The program prompts the user to enter a non-negative integer.
- **Error Handling**: A `try-except` block is used to handle invalid inputs gracefully, ensuring that only non-negative integers are accepted.

## Acknowledgements

This program provides a simple implementation of the Fibonacci sequence calculation. It is an educational tool for learning about recursion and input validation in Python.

Thank you for using the Fibonacci Number Calculator. If you find this tool useful, please share it with others and consider giving feedback.
