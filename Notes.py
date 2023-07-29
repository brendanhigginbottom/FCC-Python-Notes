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

# 1:21:16