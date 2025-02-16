#importing the Random Module in order to use the random.randint method.
import random
#setting up dictionary

#defining a function inorder for the computer to select randomly between rock, paper and scissors
def get_computer_choice():
    """
    Randomly selects from Rock, Paper or Scissors for the computer
    :return: str
    """
    return  random.choice (['Rock', 'Paper', 'Scissors'])
#defines the function as a variable
computer_choice = get_computer_choice()

#defining dictionary
choices = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

#while loop is ensuring that the user input is valid.
while True:
    user_input = input("Lets play Rock, Paper, Scissors!\nTo start enter R, P or S:").upper()
    if user_input in choices:
        user_choice = choices[user_input] #converting user choice to the full word.
        break #exit loop if input is valid
    else:
        input("You have entered an invalid option. Let's try again!\nPlease input  R, P or S:")

#this is displaying what the user and computer have chosen
print(f"You have chosen: {user_choice}")
print(f"The computer chose: {computer_choice}")

#Determining the winner
if user_choice == computer_choice: #if both choices are the same it's a draw
    print("Draw")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
    (user_choice == "Scissors" and computer_choice == "Paper") or \
    (user_choice == "Paper" and computer_choice == "Rock"):
    print("You won") #if the answers fit within this block of code the user won
else:
    print("You lost!! Let's try again'") #otherwise computer wins!