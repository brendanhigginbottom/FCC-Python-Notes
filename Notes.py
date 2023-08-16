##  Covering Basic Commands of Python

##! Variables
# assignment uses = 
# variables cannot start with a number, can't use ! or %. Also can't use keywords
name = 'Brendan'
age = 30

 ##! Expressions return values
 # 1+1 or 'Brendan'
 ## Statement is operation on a value
 ## A program is a series of statements
 # Can put multiple statements on one line separated by ; i.e., name = 'Tom'; print(name)

# Scope is defined by indentation

##! Data types
# Can check type with type(), i.e. print(type(name)) or isinstance, i.e.
# print(isinstance(name, str))
# String 'Brendan'
# Numbers - int and float print(isintance(variable, [int][float]))
# complex
# bool - boolean
# tuple - tuples
# range - ranges
# dict - dictionaries (objects(?))
# set - sets

# Can force type or cast/casting, i.e. age = float(2), age = int('20')

##! Operators
# = is assignment
# arithmatic operators +, -, *, /, %, ** (power), // (floor division rounds down)
# boolean - same as JS True/False
# boolean operators not, and, or
# i.e, condition1 = True
#      condition2 = False
#      not condition1 // False
#      condiiton1 and condition2 // False
#      condition1 or condition2 // True
    ##! Specific to or - returns first non falsy value
    ##! and returns last operand if all are falsy (last two examples below)
    ##! or put another way: if x == False, then y, else x
        #print(0 or 1) // 1
        #print(False or 'hey) // 'hey'
        #print('hi' or 'hey) // 'hi'
        #print([] or False) // False
        #print(False or []) // []
    ##! Specific to and - only evaluates second if first is true
    ##! if first is falsy (0, False, empty data types), returns that argument
    ##! and otherwise evaluates second
    ##! If x = false, then x, else y
        #print(0 and 1) // 0
        #print(1 and 0) // 0
        #print (False and 'hey') // False
        #print('hi' and 'hey') // 'hey'
        #print([] and False) // []
        #print(False and []) // False

##! bitwise operators - rarely used but worth knowing
    # & performs binary AND
    # | performs binary OR
    # ^ performs a binary XOR operation
    # ~ performs a binary NOT operation
    # << shift left operation
    # >> shift right operation

##! is - identity operator; used to compare two objects, returns True if both are same object
##! in - membershop operator; used to tell if a value is contained in a list or another sequence

##! ternary operator - write out if/else instead of condition ? truthy : falsy in JS
# def is_adult(age):
#    return True if age > 18 else False

##! Strings
# Can use both " " and ' ' 
# Can concatanate with + operator
# Can be multi-line if enclosed in three " or '
    # i.e, print("""Brendan is
    # 
    # 30
    # 
    #years old
    # """) //Brendan is
    #
    #       30
    #
    #       years old
    ##! Built in methods
    # print('Brendan'.upper()) // BRENDAN
    # print('BrenDan'.lower()) // brendan
    # print('bREndan person'.title) // Brendan Person - makes first letter capital
    # .islower() // checks if all letters are all lower
    ##! All the methods don't mutate and return new string
    ##! len() is a global function (works with multiple type of data)
    ##! and returns length
    # name = 'Brendan'
    # print(len(name)) // 7
    # print('br' in name.lower()) // True - checks substring and is case sensitive
    ##! Escaping quotes with \ -- really only needed if string needs ' and "
    # print("Bre\"ndan") // Bre"ndan 
    ##! \n = new line
    # print('Bre\nndan') // Bre
    #                       ndan
    ##! getting letter by index, can start at -1 to begin at last letter
    # print(name[0]) // B
    # print(name[-1]) // n
        ##! getting range with slicing - 
        ##! for x:y, start at index x up to (not including) index y
            # print(name[1:3]) // re

    ##! Booleans
    #bool - True or False // Note the capitalization
    #Useful with conditional control like if statements, i.e.
        # done = True
        # if done:
        #   print('yes)
        # else:
        #   print('no')
    # Numbers are always true, but 0 is always false (illustrated above)
    # Strings are false only when empty, otherwise true
    # Same for lists, tuples, sets, and dicts
    # Can check if a value is a boolean
    # print(type(done) == bool) // true

    # any
    # book_1_read = True
    # book_2_read = False
    ##! any returns true if any iterable is truthy
    # read_any_book = any([book_1_read, book_2_read]) // True

    # all
    # ingredients_purchased = True
    # meal_cooked = False
    ##! returns true if all iterables are truthy
    # ready_to_serve = all ([ingredients_purchased, meal_cooked]) // False

    ##! complex numbers
    # Extension of real number system
    # Expressed as sum of real part (int) and imaginary part (j)
    # num1 = 2+3j
    # or use complex constructor
        # num2= complex(2,3)
            # 2 is real part, 3 is imaginary (j)
        # can get real or imaginary part with:
            # print(num.real, num.imag) // 2.0 3.0
    
    ##! Functions related to numbers
    # abs()
        # abs(5.5) // 5.5
        # abs(-5.5) // 5.5
    # round()
        # round(5.5) // 6
        # round(5.49) // 5
        # Can specify precision with round(int, #)
    # A ton of libraries for numbers

##! Enums
#  Readable names bound to a constant value
#  Way to create constants in py
# from enum import Enum

# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

    # print(State.ACTIVE) // State.Active
    # print(State.AVCTIVE.value) // 1
    # print(State(1)) // State.Active
    # print(State['ACTIVE']) // State.Active
    # list all possible values
        # print(list(State))
    # count # of values stored
        # print(len(State))

##! User Input
##! Code executes up until input then waits for user input
# print("What's your age?")
# age = input()
# print(f'Your age is {age}')
##! or
# age = input("What's your age? : ")
# print(f'Your age is {age}')

##! Control Statements
    # condition = True

    # if condition == True:
        # print('The condition')
        # print('was true')
    # else:
        # print('The condition')
        # print('was False')

##! Lists
# Slightly different from arrays, list native to python
    # dogs = ['Roger', 1, 'Syd', True, 'Quincy']
    ##! in operator
    # print('Roger' in dogs) // True

    # Can reference items in list by index
        # print(dogs[0]) // Roger

    # Can update same way with array
        # dogs[1] = 2
        # print(dogs) // ['Roger', 2, 'Syd', True, 'Quincy']
    
    # extract part of list (slice)
        # print(dogs[2:4]) // ['Syd', True]
        ##! print(list[:2]) // start up to 2nd index
        ##! print(list[2:]) // 2nd index to end

    # append method
        # dogs.append('Judah') // pushes to end
    
    # extend method
        # dogs.extend(['Test'], 5) // adds list to end

    # += operator
        # dogs += [list] // same as extend, adds list to end

    ##! don't forget square brackets with extend or +=, otherwise
    ##! appends each letter in string

    # remove method
        # dogs.remove('Syd')

    # pop method
        # same as JS
        # print(dogs.pop()) // return and remove last item from list
        # print(dogs) // last value removed
    
    # add item at index n
        # items.instert(2, 'Test') // adds 'Test' to index 2

    # add with slice
        # items[1:1] = ['Test1', 'Test2'] // inserted multiple items starting at index 1
    
    # sorting lists
        # items.sort() // only works if all items in list are strings (alphabetical)
        # but begins with upper case first
        # items.sort(key=str.lower) // 
        ##! SORTING MUTATES THE LIST
            # can copy list first
                # itemscopy = items[:]
        # sorted(items, key=str.lower)
        # print(sorted) // sorted creates new list without mutating first

##! Tuples
    # Allows you to create immutable groups of objects
    # once created, can't be modified
    # created similar to list but () instead of []

names = ('Roger', 'Syd', 'Brendan')

    # print(names[0]) // 'Roger'
    # print(names.index('Syd')) // 1
    # print(names[-1]) // 'Brendan'

    # can count tuples with len
        # len(names) // 3

    # can use in same as lists
    # print('Roger' in names) // True

    # can sort tuple using sorted global function (new tuple)

    # print(sorted(names))

    # create new tuple from existing with + operator
    # newTuple = names + ('Tina', 'Ned')
    # print(newTuple)

##! Dictionaries
    # collection of key-value pairs
    # similar to JS Objects, but in py:
        # objects are sequential
        # Dictionaries are unordered
    ##! key can be any immutable value (string, number, tuple)
    ##! value can be anything
    # note spacing as convention for readability
    # dog = { 
    #     'name': 'Hohie',
    #     'age': 8,
    #     }
    # accessing with bracket notation
    # dog['name'] = 'Syd'
    # print(dog)

    # get method with dictionaries
    # print(dog.get('name')) // Hohie

    # default values with get method
    # print(dog.get('color')) // none
    # print(dog.get('color', 'brown')) // brown

    # pop method with dictionaries
    # print(dog.pop('name')) // Hohie
    # print(dog) // name: 'Hohie' removed

    # pop item method - removes and returns last k-v pair in dict
    # print(dog.popitem()) // 'age', 8

    # in operator w/ dict
    # print('name' in dog) // True
    # print('size' in dog) // False

    # keys method 
    # [dict].keys // prints keys from dict
    # w/ list (just strings)
    # list([dict].keys)

    # same can be done with values

    # list([dict].items) // returns k-v pairs in a list

    # adding to dict w/ bracket notation
    # dog['key'] = 'value' // adds to end of dict

    ##! deleting from dict
    # del dict['key'] // deletes k-v pair from dict

    # copy a dict
    # newDict = dict.copy()

##! Sets
    # work like tuples but aren't ordered and are mutable
    # or work like dictionaires but don't have keys
    # immutable set is called a 'frozen' set
    ##! think of them as mathematical sets

    # set = { 'x', 'y' } 
    ##! Uses curly brackets like dictionaries but doesn't contain
    ##! k-v pairs

set1 = {'Brendan', 'Brianna'}
set2 = {'Brendan'}

    # intersecting two sets

    # intersect = set1 & set2
    # print(intersect) // {'Brendan'}

    # union of two sets

    # 2:03:46 


