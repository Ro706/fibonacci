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
if __name__=="__main__":
    # Driver Program
    try:
        n = int(input("Enter a non-negative integer: "))
        print(Fibonacci(n))
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
