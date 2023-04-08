# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2


print(lesser(2, 4))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(str):
    list_str = str.split(' ')
    if list_str[0][0] == list_str[1][0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(num1, num2):
    total = num1 + num2
    if num1 == 20 or num2 == 20 or total == 20:
        return True
    else:
        return False


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


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
    if n in range(90, 111) or n in range(190, 211):
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
