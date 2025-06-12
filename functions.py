count = 10
def outer_function():
    count = 5
    
    def inner_function():
        count = 2
        print(f"Inner variable: {count}")
    inner_function()
    print(f"Outer variable: {count}")


print(f"Global variable: {count}")

outer_function()
