
#Password Generator Project

import string
import random

# Define the function to generate password
def password_generator(length=8):
    all_characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(all_characters) 
    for i in range(length))
    return password

# Generate a 12-character password
print("The Generated Password Is:")
print(password_generator(12))





