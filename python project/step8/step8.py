def solution(num):
    # Define a dictionary to map integer values to Roman numeral symbols
    roman_num = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 
        9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    if num < 1 or num > 3999:
        return "Invalid input"
    # Initialize an empty string to build the Roman numeral representation
    result = ""
    # Loop through the keys and build the Roman numeral representation
    for value, symbol in roman_num.items():
        while num >= value:
            result += symbol
            num -= value
    return result


print(solution(1900))

