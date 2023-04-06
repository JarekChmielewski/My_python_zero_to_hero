# for loop acts as iterator so it goes through items in a sequnce or any iterable item so
# strings, lists, tuples and even built-in iterables for dictionaries such as keys or values

#Example 1: simple for loop

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list1:
    print(num)

#Example 2: print only even numbers from list

for num in list1:
    if num%2 == 0:
        print(num)
    else:
        print("Odd number")

#Example 3: sum the list

list_sum = 0

for num in list1:
    list_sum += num

print(f"The sum of all elements in the list1 is: {list_sum}")

#Example 4: for loop with strings

for letter in "This is a string":
    print(letter)

#Example 5: for loop with a tuple

tup = (1, 2, 3, 4, 5)

for t in tup:
    print(t)

#Example 6: Tuple unpacking - When iterating through sequence that contains tuples, the item can be a tuple itself so we
# will be unpacking the tuple inside of seqence we can access items inside that tuple

list2 = [(2, 4), (6, 8), (10, 12)]

for tup in list2:
    print(tup)

#now unpacking

for (t1, t2) in list2:
    print(t1)

# Example 7: Dictionaries

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

# three Dictionary methods: .keys() .items() .values
# each of this method return a dictionary view object

print(d.items())

#unpack
for k, v in d.items():
    print(k)
    print(v)

# we can cast the view as list
print(list(d.keys()))
print(list(d.values()))

#dictionaries are unordered so we can use sorted()
print(sorted(d.values()))
