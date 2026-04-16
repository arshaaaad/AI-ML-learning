# charecter_name="arshad"
# charecter_age=22
# print("there was man named "+charecter_name+",")
# print("he was "+ charecter_age +" years old.")
# print("he really liked the name" +charecter_name+",")
# print("but he didnt like being "+charecter_age+".")

# strings

# string="Arshad is a man"
# print(string.replace("man","boy"))

# numbers

# from math import *
# print(10%2)
# print(pow(2,5))
# print(max(2,5))
# print(min(2,5))
# print(round(3.5))
# print(sqrt(36))

# getting input from user

# name=input("enter your name: ")
# age=input("enter your age : ")
# print("hello "+name+" your "+age+" years old")

# basic calci

# num1=input("enter the number")
# num2=input("enter the 2nd number")
# result=float(num1)+float(num2)
# print(result)

# madlibs

# color=input("enter the color : ")
# plural_noun=input("enter the plural noun : ")
# celebrity=input("enter the celebrity name : ")
# print("Roses are"+color)
# print(plural_noun+" are blue")
# print("I love "+celebrity)

# list

# lucky_number=[6 ,8 ,5 ,7]
# friends=["arshad","azar","ravi","kiran"]
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[0:2])
# print(friends[2:])
# friends.append(lucky_number)
# print(friends)
# friends.remove("arshad")
# print(friends)
# friends.pop()
# print(friends)
# friends.clear()
# print(friends)
# print(friends.index("arshad"))
# print(friends.count("arshad"))
# friends.sort()
# print(friends)
# friends2=friends.copy()
# print(friends2)


# tupels

# cordinates=(4,5)
# print(cordinates[0])

# # fuctions

# def say_hi(name):
#     print("hello "+name)
# say_hi("name")
# say_hi("azar")

# return statement

# def cube(num):
#     return num*num*num
# print(cube(4))

# if statements

# num1=float(input("Enter the first number : "))
# op=input("enter the operater : ")
# num2=float(input("enter the second number : "))
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("Invalid operater")

# dictionary

month_convertion={
"jan":"january",
"Feb": "February",
"Mar": "March",
"Apr": "April",
"May": "May",
"jun": "June",
"jul": "July",
"Aug": "August",
"Sep": "September",
"Oct": "October",
"Nov": "November",
"Dec": "December",
 }

print(month_convertion.get("Aug","not a valid key"))
print(month_convertion["Nov"])