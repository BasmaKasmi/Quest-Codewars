# we check whether the sum of any two sides is greater than the third side. 
def is_triangle(a, b, c):
     # If this condition is true for all sides, then a triangle can be formed.
    if a + b > c and a + c > b and b + c > a:
     # If the condition is true, we return True, otherwise False.
        return True
    else:
        return False


print(is_triangle(3, 4, 5))
print(is_triangle(1, 2, 3))
print(is_triangle(5, 1, 10))
