# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)


print(lesser(2, 4))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(str):
    list_str = str.split(' ')
    return list_str[0][0] == list_str[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(num1, num2):
    return num1 == 20 or num2 == 20 or (num1 + num2) == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(word):
    new_word = ''
    mylist = [x for x in word]
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    for item in mylist:
        new_word = new_word + item
    print(new_word)


old_macdonald('macdonald')


def old_macdonald2(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short!"


print(old_macdonald2('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    mylist = text.split(' ')
    mylist.reverse()
    new_word = ' '.join(mylist)
    print(new_word)


master_yoda('I am home')
master_yoda('We are ready')


def master_yoda2(text):
    return ' '.join(text.split()[::-1])


print(master_yoda2('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
print("LEVEL 2 : FIND 33")


def has_33(mylist33):
    for num in range(0, len(mylist33) - 1):
        if mylist33[num] == 3 and mylist33[num + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(str):
    mylist = [x * 3 for x in str]
    return ''.join(mylist)


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(n1, n2, n3):
    total = n1 + n2 + n3
    if total <= 21:
        return total
    elif total <= 31 and 11 in (n1, n2, n3):
        return total - 10
    else:
        return "BUST"


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

print("SUMMER 69")


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(mylist):
    total = 0
    for i in mylist:
        if i in range(6, 10):
            i = 0
        total += i
    return total


# this is not perfectly correct solution -> look for def2 below
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 7, 9, 7, 11]))


def summer_69_2(mylist):
    total = 0
    add = True
    for number in mylist:
        while add:
            if number != 6:
                total += number
                break
            else:
                add = False
        while not add:
            if number != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69_2([1, 3, 5]))
print(summer_69_2([4, 5, 6, 7, 8, 9]))
print(summer_69_2([2, 1, 6, 7, 9, 7, 11]))
# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
print("SPY GAME:")


def spy_game(mylist):
    new_list = [str(number) for number in mylist if number in (0, 7)]
    return ''.join(new_list) == '007'


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.
print("COUNT PRIMES:")


def count_primes(number):
    primes = []
    if number > 1:
        for x in range(2, number):
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                primes.append(x)
    return len(primes)


print(count_primes(100))
