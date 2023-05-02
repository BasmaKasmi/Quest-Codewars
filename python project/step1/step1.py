def math_op(op, value1, value2):
    if op == "+":
        return value1 + value2
    elif op == "-":
        return value1 - value2
    elif op == "*":
        return value1 * value2
    elif op == "/":
        if value2 == 0:
            return "Cannot divide by zero"
        else:
            return value1 / value2
    else:
        return "Invalid op"
    
print(math_op("+", 5, 3))  # output: 8
print(math_op("-", 7, 2))  # output: 5
print(math_op("*", 4, 6))  # output: 24
print(math_op("/", 10, 2))  # output: 5.0
print(math_op("/", 10, 0))  # output: "Cannot divide by zero"
print(math_op("!", 3, 4))  # output: "Invalid op"



# the function takes three arguments: the operation to be performed (+, -, *, or /)

# the two values to operate on. The function then checks which operation was requested and performs it on the two values. 

# If an invalid operation is requested, the function returns an error message.
