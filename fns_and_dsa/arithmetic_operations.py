def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    int or float: The result of the operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', 'divide'.")