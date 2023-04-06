# range - generate a list of integers with 3 parameters start, stop and step
# this is a generator function so to get a list we need to cast wuth list()

x = list(range(0, 11))
print(x)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = list(range(0, 11, 2))
print(y)
# [0, 2, 4, 6, 8, 10]

z = list(range(0, 101, 10))
print(z)
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]