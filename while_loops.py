# while loop is one of most general ways to perform iteration
# runs as long as condition is True

# Example 1: simple while loop

x = 0

while x < 10:
    print(x)
    x += 1

else:
    print("All done!")

# break, continue, pass

# break - breaks out of the current closest enclosing loop
# continue - goes to the top of the closest enclosing loop
# pass - does nothing at all

x = 0

while x < 10:
    print(f"x is currently {x}")
    print("adding 1 to x as x is still less than 10")
    x += 1
    if x == 3:
        print("x==3")
        break
    else:
        print('continuing...')
        continue
