import random
def get_choices():
    player_choice=input("enter a choice(rock.paper,scissors:)")
    options=["stone","paper","scissors"]
    computer_choice=random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player} ,computer chose {computer}")
    if player==computer:
        return "it's a tie"
    elif player=="rock" :
        if computer=="scissors":
            return "rock smashed scissors you WIN"
        else:
            return "paper covered rock you lose"
    
    elif player=="paper" :
        if computer=="scissors":
            return "scissors cut the paper you lose"
        else:
            return "paper covered rock you WIN!"
    
    elif player=="scissors" :
        if computer=="paper":
            return "scissors cut the paper you WIN!"
        else:
            return "rock smashed the scissors you lose"

choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print (result)


    

                   