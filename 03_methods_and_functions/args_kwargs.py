def myfunc(a, b):
    return sum((a, b)) * .05


print(myfunc(40, 60))


# Notice also that to work with multiple positional arguments in the sum() function we had to pass them in as a tuple.
# What if we want to work with more than two numbers?
# One way would be to assign a lot of parameters, and give each one a default value.

def myfunc(a=0, b=0, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * .05


print(myfunc(40, 60, 20))

# We dont want to do above as this is not very efficient solution so that is where *args comes in so

def myfunc(*args):
    return sum(args)*.05


print(myfunc(40, 60, 20))

# we can use other word instead of args as long as preceded by an *


def myfunc(*spam):
    return sum(spam)*.05


print(myfunc(40, 60, 20))

# KWARGS - instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favourite fruit is {kwargs['fruit']}")
    else:
        print("I dont like fruit")


myfunc(fruit='pineapple')
myfunc()


# *args and **kwargs - you can pass both in this same function but *args have to appear before **kwargs

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favourite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')