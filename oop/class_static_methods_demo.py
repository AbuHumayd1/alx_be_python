# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print calculation type and return the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    result_add = Calculator.add(5, 3)
    print(f"Addition result: {result_add}")

    # Using class method
    result_multiply = Calculator.multiply(5, 3)
    print(f"Multiplication result: {result_multiply}")
