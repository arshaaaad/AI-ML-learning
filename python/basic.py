# name="arshad"
# age="22"
# print ("my name is "+name+ " my age is " +age)

# print(type(age))
# print(isinstance(name , str))
# age=float(2)
# print(isinstance(age , int))


# arithmatic operater
#     a+b
#     a-b
#     a*b
#     a/b
#     a**b
#     a//b
#     a%b
#     comperation operator
# a==b
# a!=b
# a>b
# a<=b

# #boolean operator
# condion1=True
# condition2false=False

# not condion1
# condition1 and condition2
# condition1 or condition2

# name= "arsha"
# print(name.lower())
# print(name.upper())
# print(len(name))
# print("sh" in name)
# print("arshad \n\"arshad\"")


# name= "arshad"
# print(name[2])

# name= "arshad"
# print(name[0:5])

# done=True
# print(type(done)==bool)

# if done:
#     print("yes")
# else:
#     print("false")


# complex=2+3j
# num=complex(2,3)

# print(num.real)
# print(num.imag)

# print(abs(5.5))
# print(abs(-5.5))
# print(round(5.5))
# print(round(5.59,1))

# from enum import Enum
# class state(Enum):
#     INACTIVE=0
#     ACTIVE=1
# print(state(1))

# print("what is your age")
# age=input()
# print("your age is "+age)

# cats=["minnu",2,"ammu",20,"mani",125,True]


# print(cats[4])
# print(cats[2:5])
# cats.append("arsha")
# print(cats)
# cats.extend(["chimmi",12])
# print(cats)

# cats[2]="bean"

# cats.remove("mani")

cats=["minnu","2","ammu","20","mani","125","True"]
catscopy=cats[:]
cats.insert(3,"test")
print("cats")
print(catscopy)
cats[1:1]=["test1","test2"]
cats.sort(key=str.upper)
print(cats)
