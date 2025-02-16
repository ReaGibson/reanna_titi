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
#defines the function as a veriable
computer_choice = get_computer_choice()

choices = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

while True:
    user_input = input("Lets play Rock, Paper, Scissors!\nTo start enter R, P or S:").upper()
    if user_input in choices:
        user_choice = choices[user_input]
        break
    else:
        input("You have entered an invalid option. Let's try again!\nPlease input  R, P or S:")

print(f"You have chosen: {user_choice}")
print(f"The computure chose: {computer_choice}")

#Determining the winner
if user_choice == computer_choice:
    print("Draw")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
    (user_choice == "Scissors" and computer_choice == "Paper") or \
    (user_choice == "Paper" and computer_choice == "Rock"):
    print("You won")
else:
    print("You lost!! Let's try again'")