I'd be glad to create a README.md file for the provided code:

**Fibonacci Sequence Calculator**

This Python program calculates the nth Fibonacci number using recursion.

**What is the Fibonacci Sequence?**

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers. The first two numbers in the sequence are conventionally 0 and 1. Here are the first few Fibonacci numbers:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

**How to Use This Program**

1. **Run the program:** Save the code as a Python file (e.g., `fibonacci.py`). Then, open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

   ```bash
   python fibonacci.py
   ```

2. **Enter a non-negative integer:** The program will prompt you to enter a non-negative integer (n). This represents the position of the Fibonacci number you want to calculate. For example, if you enter 5, the program will return 5 (the fifth Fibonacci number).

**Example:**

```
Enter a non-negative integer: 8
34
```

**Error Handling**

- If you enter a negative number, the program will display an error message indicating "Incorrect input."
- If you enter a non-numeric value, the program will display an error message indicating "Invalid input. Please enter a non-negative integer."

**Code Explanation**

The code defines a recursive function `Fibonacci(n)` that calculates the nth Fibonacci number. The function works as follows:

- **Base cases:**
  - If `n` is 0, the function returns 0 (the first Fibonacci number).
  - If `n` is 1, the function returns 1 (the second Fibonacci number).
- **Recursive case:**
  - For `n` greater than 1, the function calculates the nth Fibonacci number by recursively calling itself with `n-1` and `n-2` (the previous two Fibonacci numbers) and adding their results.

The driver program prompts the user for input, handles potential errors, and calls the `Fibonacci(n)` function to calculate and print the result.
