import random
def roll_dice(dies,sides):
    roll=[]

    for i in range (0,dies):
       face=random.randint(1,sides)
       roll.append(face)
       return roll

dies=int(input("enter the number of dies :" ))
if dies<=0:
    print("you atleast want one dies ")
    quit()
sides=int(input("enter the sides"))
if sides<=0:
    print("you atleast want one dies ")
    quit()
roll=list(roll_dice(dies,sides))
print(roll)