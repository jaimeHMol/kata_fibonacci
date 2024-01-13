
def fibonacci(num_fibonacci:int = 10) -> list:
    """ Generates the Fibonacci series of numbers up to the num_fibonacci received as
    input. """

    # Validate inputs
    if num_fibonacci <= 0 or not type(num_fibonacci) == int:
        raise ValueError("The Fibonacci number must be a positive integer greater than 0.")

    num1 = 0
    num2 = 1
    fibonacci_series = []
    fibonacci_series.append(num1)
    fibonacci_series.append(num2)
    for i in range(num_fibonacci - 2):
        prev_num2 = num2
        num2 = num1 + num2
        num1 = prev_num2
        fibonacci_series.append(num2)

    return fibonacci_series
