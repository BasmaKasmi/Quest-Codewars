# Quest Codewars

// step 1:

The function uses an if-elif statement to determine which operation to perform based on the input operator. 
The corresponding mathematical operation is then applied to the input values and the result is returned. 
The function assumes that the input values are both numbers and that the input operator is one of the four basic mathematical 
operators (+, -, *, /).

// step 2:

The function simply multiplies the input time by 0.5 and rounds down to the nearest integer using the math.floor() method, 
since Nathan drinks 0.5 litres of water per hour of cycling.

// step 3:

The function take an integer n as input, and return a list of integers from 1 up to n. 
We use the range() function to generate a sequence of numbers from 1 up to n, and the append() method to add each number to the monkeys list. Alternatively, we use a list comprehension to generate the list directly.

// step 4:

Here's how the function works:

* It defines a list of lowercase vowels.
* It creates a new string by iterating over each character in the input string, checking if the character is not in the list of vowels, 
    and adding it to the new string if it is not a vowel.
* It returns the new string.

// step 5:

This function takes a number as input and returns the squared digits concatenated together.
For example, square_digits(9119) returns 811181, and square_digits(765) returns 493625.

The function works by converting the input number to a string and iterating over each digit. For each digit, it squares the value (using the exponentiation operator **) and appends the result to a string. Finally, the function returns the string as an integer.

// step 6:
According to the triangle inequality theorem, the sum of any two sides of a triangle must be greater than the third side. 
Therefore, to check if a triangle can be built with the given side lengths, we need to check if the sum of any two sides is greater than the third side. If this condition is satisfied for all sides, we return True, otherwise, we return False.

Additionally, we add a check to make sure the surface area of the triangle is greater than 0. This is because triangles with zero or negative surface area do not exist.

// step 7:

The function first checks if the array has 0 or 1 elements, in which case it is already considered to be in ascending order. 
Otherwise, it iterates through the array and checks if each element is less than or equal to the next element.

If it finds a pair of adjacent elements where the left element is greater than the right element, it returns False. 

If it makes it through the entire loop without finding such a pair, it returns True.

// step 8:

The function first defines a dictionary of Roman numerals and their corresponding values. It then checks if the input number is within the specified range (1 to 3999). 

If the input number is valid, the function converts the number to Roman numerals using a loop that iterates through the dictionary and subtracts the corresponding value from the input number as long as it is greater than or equal to that value. 

Finally, the function returns the resulting string of Roman numerals.

// step 10:

The function starts by initializing a score of 0 and an array of counts for each die value (1-6) to 0. 
It then iterates through the input array of dice and counts the number of occurrences of each die value using the counts array.

Next, it checks the counts array for triplets of each die value (1-6). If it finds a triplet, it adds the corresponding number of points to the score and subtracts 3 from the count for that die value in the counts array.

Finally, it adds points for any remaining 1s and 5s in the counts array and returns the total score.

