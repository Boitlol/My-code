import random
import string


password_length = int(input("Enter the desired password length: "))


characters = string.ascii_letters + string.digits + string.punctuation

password = []


for i in range(password_length):
    password.append(random.choice(characters))

password_list =""

for char in password:
    password_list += char

print(f"The generated password is :{password_list}")
