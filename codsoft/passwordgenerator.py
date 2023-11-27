#/password generator in python made by dhanush
import string
import random

up_letters = list(string.ascii_uppercase)
low_letters = list(string.ascii_lowercase)
numbers = ['1','2','3','4','5','6','7','8','9','0']
Symbols = ['!','@','#','$','%','^','&','*',]

no_upletters = int(input("How many upper case letter you wanna need :"))
no_lowletters = int(input("How many lower case letter you wanna need :"))
no_numbers = int(input("How many numbers you wanna need :"))
no_symbols = int(input("How many case-sensitive symbols you wanna need :"))

password = ""


for char in range(1, no_upletters+1):
    password += random.choice(up_letters)

for char in range(1, no_lowletters+1):
    password += random.choice(low_letters)

for char in range(1, no_numbers+1):
    password += random.choice(numbers)

for char in range(1, no_symbols+1):
    password += random.choice(Symbols)

print(password)
user = input("do you wanna jumble it one(y/n):")
mix_password = ""
if user == 'y':
    for char in range(1, len(password)):
      mix_password +=random.choice(password)
    print(mix_password)

elif user == 'n' :
    print(password)

else :
    print("enter valid choice either y oy n")

    


