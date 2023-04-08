# Use for , .split() and if to create a statement that will print words that start with 's'

st = 'Print only the words that start with s in this sentence'

lst = st.split(' ')
for i in lst:
    if i[0] == 's':
        print(i)
print(lst)

# Use range to print all the even numbers from 0 to 10

for i in range(0,11):
    if i % 2 == 0:
        print(i)

# we can do it in one line ->
print(list(range(0, 11, 2)))

# Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

lst1 = [x for x in range(1, 51) if x % 3 == 0]
print(lst1)

# Go through the sting below and if the length of the word is even print "even"

st = 'Print every word in this sentence that has an even numer of letters'

for i in st.split(' '):
    if len(i) % 2 == 0:
        print(f"{i} is even")

# write a program that prints integers from 1 to 100.
# For multiples of 3 print "Fizz" instead of number, for multiple of 5 print "Buzz"
# For multiples of both 3 and 5 print "FizzBuzz"

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# Use list comprehension to create a list of the first letters of every word in the string below

st = 'Create a list of the first letters of every word in this string'

lst3 = [x[0] for x in st.split(' ')]
print(lst3)