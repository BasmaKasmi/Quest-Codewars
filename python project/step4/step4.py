def shortcut(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_s = ''
    for char in s:
        if char.lower() not in vowels:
            new_s += char
    return new_s



print(shortcut("hello"))
print(shortcut("codewars"))
print(shortcut("goodbye"))
print(shortcut("HELLO"))

# The function takes a string s as its input and creates a list of vowels. 
# It then iterates over each character in the input string s and checks whether it is a lowercase vowel. If it is not a vowel, the character is added to a new list.
# the function joins the characters in the new list and returns the resulting string with all lowercase vowels removed.