# Here is code for pasword generator
# step 1- importing random
import random

# step 2- create variable that help to genrate password
#
caps_small = ['a','b','c','d','e','f','g','h','i','j','k'
              ,'l','m','n','o','p','q','r','s','t'
              ,'u','v','w','x','y','z','A','B','C','D'
            ,'E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','%','^','&','*','(',')','+','?']

#
print("Welcome to the Py-Passwors Generator!")
num_of_letter = int(input("How many letter would you wants in your password\n- "))

num_Of_symbol = int(input(f"How many symbols would you like?\n- "))

num_of_number = int(input(f"How many numbers would you like?\n- "))


password = []
for char in range(1,num_of_letter +1):
    password += random.choice(caps_small)


for char in range(1, num_Of_symbol + 1):
    password += random.choice(symbol)


for char in range(1, num_of_number + 1):
    password += random.choice(number)

print(password)
random.shuffle(password)
print(password)

password1_list = ""

for char in password:
    password1_list += char

print(f'Your Password is \n {password1_list}')
