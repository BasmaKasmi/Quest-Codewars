def square_digits(num):
    result = ''
# Loop through each digit and square it
    for digit in str(num):
        result += str(int(digit) ** 2)
    return int(result)




print(square_digits(9119))
print(square_digits(765))

