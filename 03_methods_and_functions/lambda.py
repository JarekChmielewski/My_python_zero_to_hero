# MAP FUNCTION
# allows to map a function to iterable object such as list
print("MAP function")
def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

map(square, my_nums)
# to get a results we need to iterate through map() or cast it to list
print(list(map(square, my_nums)))


# Example 2

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]


mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']

print(list(map(splicer, mynames)))

# FILTER FUNCTION -
print("FILTER function")


def check_even(num):
    return num % 2 == 0


nums = [x for x in range(0, 11)]
print(nums)

print(list(filter(check_even, nums)))

# LAMBDA expresion - allows to create ad-hoc functions without define function using def
# lambda body is a single expression not a block of statements so we use it for simple functions
print("LAMBDA function")


def square(num):
    result = num ** 2
    return result


print(square(2))


# we could simplyfy this into one line

def square(num): return num ** 2


print(square(2))

# now using lambda

lambda num: num ** 2
# we wont assign a name to lambda expression
# we use this when we need a function we are passing once into function passed in such as map or filter

print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))

# the more complex functions are the harder it is to translate to lambda or it is impossible
# grab first character of a string
lambda s: s[0]

# reverse a string
lambda s: s[::-1]

# multiple arguments lambda
lambda x,y : x+y