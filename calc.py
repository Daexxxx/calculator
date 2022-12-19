def calculator():
  while True:
    # Get the user's input
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    
    # Check if the user has entered a valid operator
    if operator == '+':
      result = float(num1) + float(num2)
    elif operator == '-':
      result = float(num1) - float(num2)
    elif operator == '*':
      result = float(num1) * float(num2)
    elif operator == '/':
      result = float(num1) / float(num2)
    else:
      result = "Invalid operator"
    
    # Print the result
    print(result)
    
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (Y/N) ")
    if choice.lower() == 'n':
      break

# Run the calculator
calculator()
