def count_monkeys(n):
    monkeys = []
    for i in range(1, n+1):
        monkeys.append(i)
    return monkeys


print(count_monkeys(5))

print(count_monkeys(10))

print(count_monkeys(1))


# range(1, n+1) generates a sequence of numbers from 1 to n.

# The list comprehension [i for i in range(1, n+1)] creates a list by iterating over the sequence of numbers generated by range() 

# and adding each number to the list.

# The resulting list is assigned to the variable numbers.

# The print() function displays the list on the screen.

# The append() method in Python adds a single element to the end of a list. 