# Function is a group of statements that can be run more than once so don't repeat our code
# We could also specify parameters as inputs for our function

# simple function

def say_hello():
    print("Hello")


say_hello()


# simple function with argument
def greeting(name):
    print(f"Hello {name}")


greeting("Jarek")


# return lets us use a result of a function - to store as variable or use it other way

def add_num(num1, num2):
    return num1 + num2


suma = add_num(4, 5)
print(suma)

print(add_num('one', 'two'))


# so difference between print() and return is simply that by using return we can use result and save it as variable
# but by using print() we can only display result

def print_result(a, b):
    print(a + b)


def return_result(a, b):
    return a + b


# we display result
print_result(10, 5)
# we dont display
return_result(10, 5)

my_result = print_result(20, 30)
print(type(my_result))
# <class 'NoneType'> --> so we didnt save result to variable
my_result = return_result(20, 40)
print(type(my_result))


# <class 'int'> - we have integer


# check if a number is even and return boolean -> 20%2 => 0 so 20%2 == 0 => True

def even_check(number):
    return number % 2 == 0


print(even_check(20))
print(even_check(21))


# Check if any number from given list is even

def even_check_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass


# this is not a solution as we return NONE by giving only odds numbers
print(even_check_list([1, 5, 3]))


def even_check_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            return False


# It will give True or False based on first numer from list and not checking others
print(even_check_list([1, 2, 3]))


# so correct solution is to return False after for loop is over

def even_check_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
    return False


print("correct even_check_list: ")
print(even_check_list([1, 5, 3]))


# return all even numbers in a list

def return_all_even(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


print(return_all_even([1, 2, 3, 4, 5, 6, 7]))

# return tuples for unpacking

stock_prices = [('APPL', 200), ('GOOG', 300), ('MSFT', 400)]

for i in stock_prices:
    print(i)

for stock, price in stock_prices:
    print(stock)
    print(price)

# functions often returns tuples to easily have multiple results for later use
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]


# find employee of the month based on number of worked hours

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return employee_of_month, current_max


print(employee_check(work_hours))

# Interactions between functions

example = [1, 2, 3, 4, 5]
from random import shuffle

shuffle(example)
print(example)

# simple game

mylist = ['', 'O', '']


def shuffle_list(mylist):
    shuffle(mylist)

    return mylist


shuffle_list(mylist)
print(mylist)


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick you number: 0, 1 or 2 ")

    return int(guess)


print(player_guess())

# now interaction between two functions

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct !')
    else:
        print("Wrong !")
        print(mylist)

mylist = ['', 'O', '']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mylist, guess)