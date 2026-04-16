import random
lower_number=1
higher_number=100
computer_guess=random.randint(lower_number,higher_number)
user_input=0
print("welcome to Python number guessing game")

 
while computer_guess!=user_input:
    user_input=int(input(f"Enter the nuber between {lower_number} and {higher_number}: "))
    if user_input > computer_guess:
        print("too high")
    elif user_input < computer_guess:
        print("too low")
    else :
        print("you win")




