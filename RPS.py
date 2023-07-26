#imports in py - seems no different
import random


# Functions declared with def
# Function scope defined by indentation
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win():
  


## List and example of calling method from random library
# testList = ['one', 'blue', 'no']
# output = random.choice(testList)
# print(output)



# def greeting():
#   return 'Hi'

# Can assign variable to function return value like in JS
# response = greeting()

# print(response)