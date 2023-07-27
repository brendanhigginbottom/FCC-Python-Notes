#imports in py - seems no different
import random

# Functions declared with def
# Function scope defined by indentation
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

##Passing arguments in py
def check_win(player, computer):
  print(f"You chose {player}. Computer chose {computer}.")
  ##if statement called with : after condition
  ##elif for else if
  ## and instead of && for py
  if player == computer:
    return("It's a tie!")
  elif player == 'rock':
    if computer == 'scissors':
      return('Rock smashes scissors! You win!')
    else: 
      return('Paper covers rock. You lose!')
  elif player == 'paper':
    if computer == 'rock':
      return('Paper covers rock! You win!')
    else: 
      return('Scissors cuts paper. You lose!')
  elif player == 'scissors':
    if computer == 'paper':
      return('Scissors cuts paper! You win!')
    else: 
      return('Rock smashes scissors. You lose')

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)

## List and example of calling method from the Random library
# testList = ['one', 'blue', 'no']
# output = random.choice(testList)
# print(output)

## Same as in JS, = is assignment
## and == checks equality. Also !=, <=, >=

## F Strings - template literal equivalent
# age = 25
# print(f"Jim is {age} years old.")



# def greeting():
#   return 'Hi'

# Can assign variable to function return value like in JS
# response = greeting()

# print(response)