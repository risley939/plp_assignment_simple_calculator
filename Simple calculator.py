# A simple calculator program that performs a mathematical operation
# on two user-provided numbers.

def calculator():
    """
    Asks the user for two numbers and an operator, then calculates and
    prints the result.
    """
    print("Welcome to the simple Python Calculator!")

    try:
        # Get the first number from the user and convert it to a float.
        num1 = float(input("Enter the first number: "))
        
        # Get the second number from the user and convert it to a float.
        num2 = float(input("Enter the second number: "))

        # Get the desired operation from the user.
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform the calculation based on the operator.
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Check for division by zero before performing the operation.
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return # Exit the function to prevent further execution.
            else:
                result = num1 / num2
        else:
            # Handle invalid operator input.
            print("Error: Invalid operator. Please use +, -, *, or /.")
            return # Exit the function.

        # Print the final result in the requested format.
        # The f-string is used for easy formatting.
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        # Handle cases where the user enters non-numeric input.
        print("Error: Invalid input. Please enter valid numbers.")

# Call the function to run the calculator.
calculator()
