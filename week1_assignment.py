
# Input function to enter numbers and operation;

num_1 = float(input("Enter the first number: "))
num_2 = float(input ("Enter the second number: "))
operation = input("Enter the operation(+, -, * or /)")

#To perform different operations;

if operation == "+":
    result = num_1 + num_2
elif operation =="-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    if num_2 ==  0:
        result = "Error! Cannot divide by zero"
    else:
        result = num_1 / num_2
else: 
    result = "Error! Invalid Operation"

# Print the result;

print("Result: ", result)




