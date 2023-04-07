# RANGE - generate a list of integers with 3 parameters start, stop and step
# this is a generator function so to get a list we need to cast with list()

x = list(range(0, 11))
print(x)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = list(range(0, 11, 2))
print(y)
# [0, 2, 4, 6, 8, 10]

z = list(range(0, 101, 10))
print(z)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# ENUMERATE - useful function with for loops that keeps track of loop_count variable

index_count = 0

for letter in 'abcde':
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1

#enumerate - notice tuple unpacking

for i, let in enumerate('abcde'):
    print(f"At index {i} the letter is {let}")

# ZIP - it is a generator

# notice the format enumerate returns and let's transform it to a list
print(list(enumerate('abcde')))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
# It was a list of tuples so we can use tuple unpacking during a for loop.
# We can use zip function to quickly create a list of tuples by zipping up together two lists

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
x = zip(mylist1, mylist2)
print(list(x))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# to use generator we can use for loop

for item1, item2 in zip(mylist1, mylist2):
    print(f"For this tuple first item is {item1} and second is {item2}")

# IN and NOT IN OPERATORs

'x' in ['x', 'y', 'z']
# True
'x' in [1, 2, 3]
#False

'x' not in ['x', 'y', 'z']
# False
'x' not in [1, 2, 3]
# True

# MIN and MAX

mylist3 = [10, 20, 30, 100]
print(min(mylist3))
print(max(mylist3))

# RANDOM

from random import shuffle
# this will shuffle a list in-place so it wont return anything but it will effect list passed
shuffle(mylist3)
print(mylist3)

from random import randint
# it will return random integer in range including both ends so 0 and 10 included
print(randint(0, 10))

# INPUT - ask user for a value of a parameter
input("Input something here: ")
