container = [23,34,55,66,98,78,56,88,99,34]
#how to find maximum no using loop
max_num = container[0]
for i in container:
    if i > max_num:
        max_num = i

print(f"max no is {max_num}")
#how to add no from 1 to 100 using for loop with range function
#we use range in which list is not given to us, but two limits upper and lower is given
count = 0
for i in range(1,100):
    count = count+i
print(f'total count is {count}')

"""Generate Strong password """
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Code_with_me_Password Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))


# password = ""
# for i in range(0,num_of_letters):
#     password += random.choice(letters)
#
# for i in range(0,num_of_symbols):
#     password += random.choice(numbers)
#
# for i in range(0,num_of_numbers):
#     password += random.choice(symbols)
#
# print(f"YOUR PASSWORD IS : {password}")

#hard level password
password_list = []
for i in range(0,num_of_letters):
    password_list += random.choice(letters)

for i in range(0,num_of_symbols):
    password_list += random.choice(numbers)

for i in range(0,num_of_numbers):
    password_list += random.choice(symbols)

print(password_list)
#we have to shuffle it into random orders to make it strong
print(random.shuffle(password_list))
print(f"YOUR PASSWORD IS : {password_list}")

#let us turn it back to sting as it is in list form
password = ""
for i in password_list:
    password += i
print(f"Your password is {password}")



