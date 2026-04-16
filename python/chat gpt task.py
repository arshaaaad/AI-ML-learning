# vovels={"a","e","i","o","u"}
# user_input=input("enter the word :").lower()

# if " " in user_input:
#     input=del(" ") from user_input

# print(input)


# vovels_count=0
# for user_input in vovels:
#     vovels_count+=1
# print(vovels_count)


# number=int(input("enter a number"))
# sum=number%2
# if sum==0:
#     print("it is even numebr")
# else:
#     print("it is odd number")


# word=input("enter the word ")
# r_word=' '.join(words[::-1]for words in word.split())
# print(r_word)


vovels={"a","e","i","o","u"}
word=input("enter the word :")
vovels_count=0
for char in word:
    if char in vovels:
        vovels_count+=1
    

print(vovels_count)