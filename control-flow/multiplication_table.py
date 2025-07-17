"""


user_input = int(input("Enter a number to see its multiplication table: "))

def multiplication_table(user_input):
    print(f"Multiplication Table for {user_input}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

multiplication_table(user_input)
"""""
def multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

user_input = int(input("Enter a number to see its multiplication table: "))
multiplication_table(user_input)
