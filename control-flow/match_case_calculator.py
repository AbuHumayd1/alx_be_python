num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ").strip()
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    case "/":
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
    case _:
        print("Invalid operation. Please enter one of +, -, *, or /.")