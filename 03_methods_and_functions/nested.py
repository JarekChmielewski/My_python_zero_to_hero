x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# This idea of scope in your code is very important to understand in order to properly assign and call variable names.
#
# In simple terms, the idea of scope can be described by 3 general rules:
#
# 1. Name assignments will create or change local names by default.
# 2. Name references search (at most) four scopes, these are:
#   - local
#   - enclosing functions
#   - global
#   - built-in
# 3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
# The statement in #2 above can be defined by the LEGB rule.
#
# LEGB Rule:
#
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda),
# from inner to outer.
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

# LOCAL
f = lambda x: x ** 2
# x is local

# ENCLOSING FUNCTION LOCALS - when we have function inside function
name = 'This is a global name'


def greet():
    # enclosing function
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()


greet()

# GLOBAL
print(name)

# BUILT-IN for example "len" function

# LOCAL VARIABLES - all variables have a scope of the block they are declared in and they are not related to variables
# with this same names outside the function

x = 50


def func(x):
    print(f"x is: {x}")
    x = 2
    print(f"Changed local variable x to: {x}")


func(x)
print(f"x is still: {x}")


# THE GLOBAL STATEMENT - we can assign value using global
print("THE GLOBAL STATEMENT: ")
x = 50


def func():
    global x
    print("This function is now using the global x!")
    print(f"Because of global x is: {x}")
    x = 2
    print(f"Ran func(), changed global x to {x}")


print(f"Before calling func(), x is {x}")
func()
print(f"Value of x (outside of func()) is {x}")