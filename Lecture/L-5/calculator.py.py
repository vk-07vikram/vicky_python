# simple calculator using ladder statements

operator = input("Enter an Operator(+ , - , * , / )")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter secound number : "))

# perform for calculation

if operator == '+':
    result = num1 + num2
    print(f"sum of {num1} + {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"sum of {num1} * {num2} = {result}")
else:
    print(f"sum of {num1} - {num2} = {result}")
