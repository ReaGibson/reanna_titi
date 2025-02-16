
import random # importing random module. In this case, the random.randint would help pick random nos between 0 -2


#prompt the user to enter a value: R, P, S. Upper method added incase the user uses lowercase r,p or s.
user_input = input("let's play! Enter R, P, or S: ").upper()
print(user_input)

#by using the if statement, we are determining R,P,S and converting the characters into rock, paper and scissors.

if user_input == "R":
    user_input = "rock"
    print(f"You chose:{user_input}") #helps shows the user choice
elif user_input == "P":
    user_input = "paper"
    print(f"You chose:{user_input}")
elif user_input == "S":
    user_input = "scissors"
    print(f"You chose:{user_input}")
else:
   input ("Wrong code. Let's try again - Please input R, P or S:") #incase a wrong character




computer_input = random.randint(0, 2) #randint generates a random integer between 0 and 2.
#if statements are determining the integers and converting them to rock, paper and scissors.
if computer_input == 0:
    computer_input = "rock"
    print(f"Computer chose: {computer_input}") #helps shows the computer choice
elif computer_input == 1:
    computer_input = "paper"
    print(f"Computer chose: {computer_input}")
else:
    computer_input = "scissors"
    print(f"Computer chose: {computer_input}")


if user_input == computer_input:
    print("Draw")
elif user_input == "rock" and computer_input == "scissors":
    print("You won")
elif user_input == "scissors" and computer_input == "paper":
    print("You won")
elif user_input == "paper" and computer_input == "rock":
    print("You won")
else:
    print("You lost!! Let's try again'")







