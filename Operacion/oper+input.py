import math

def integer_calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            return
    else:
        print("Invalid operation")
        return

    # Round the result down to the nearest integer
    result = math.floor(result)
    print(f"{num1} {operation} {num2} = {result}")

# Call the function
integer_calculator()