# one line for loop to build lists

lst = [x for x in 'word']
print(lst)

# EXAMPLE 1: list of numbers squered in range 0 to 11

lst1 = [y ** 2 for y in range(0, 11)]
print(lst1)

# EXAMPLE 2: with if statements - check for even numbers in a range

lst2 = [z for z in range(11) if z % 2 == 0]
print(lst2)

# EXAMPLE 3: convert Celsius to Fahrenheit

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5)*temp+32) for temp in celsius]
print(fahrenheit)

# EXAMPLE 4: nested list comprehensions

lst4 = [x**2 for x in [x**2 for x in range(11)]]
print(lst4)