import string
import random
import time
from pathlib import Path

print(r"""
    ____                                          __                                    __            
   / __ \____ ____________      ______  _________/ /  ____ ____  ____  ___  _________ _/ /_____  _____
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /  / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/   \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                   /____/                                             
""")

length=int(input("Enter the length of the password: "))
site=input("Enter the site name: ")

lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
numbers=string.digits
special="!@#$%^&*()_+-=[]{}|;:,.<>?"
password=""
password_file=Path.home() / "Desktop" / "passwords.txt"

if length<4:
    print("Password length must be at least 4 characters.")
else:
    password+=random.choice(lowercase)
    password+=random.choice(uppercase)
    password+=random.choice(numbers)
    password+=random.choice(special)

    for i in range(length-4):
        password+=random.choice(lowercase+uppercase+numbers+special)

    with open(password_file, "a") as file:
        file.write(f"{site}: {password}\n")
        file.write("==============================================================================\n")


print(f"Generated password for {site} is {password}")
print("Closing the program in 2 seconds...")
time.sleep(2)
print("Closing the program...")
