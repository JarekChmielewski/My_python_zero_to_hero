# Let's use while loop to create guessing game

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

from random import randint
random_number = randint(1, 100)
game_is_on = True
turn_count = 0
last_diff = 0

while game_is_on:
    guess = int(input("Please guess a number: "))
    turn_count += 1
    diff = abs(random_number - guess)
    if diff == 0:
        print(f"Guessed correctly. It took {turn_count} guesses")
        break
    elif guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    elif turn_count == 1:
        if diff > 10:
            print("COLD")
        else:
            print("WARM")
    else:
        if last_diff < diff:
            print("COLDER!")
        else:
            print("WARMER!")
    last_diff = diff



