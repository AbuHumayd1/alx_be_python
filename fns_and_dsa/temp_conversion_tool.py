
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted:.2f}°C")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError as e:
    print(f"Error: {e}")


