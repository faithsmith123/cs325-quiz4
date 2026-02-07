number1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
userOperator = (input("Please enter the operation you with to do: (+, -, *, /)"))




elif userOperator == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(float(num1) / float(num2))