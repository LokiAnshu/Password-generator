# Introduction
print('Hello and welcome to Password Generator')
print('Please answer the following to generate a unique password')
print('')

# Pool of characters 
alphabets_lower = list("abcdefghijklmnopqrstuvwxyz")
alphabets_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = list("1234567890")
s_ch = list("!@#$%^&*()-_=+")

# Specifications and adding atleast one of the characters from each of the chosen options
while True:
    try:
        password_length = int(input('Password length: '))
        break
    except ValueError:
        print('Please enter a number')


import random
random_password=[]

while True:
    print('Include uppercase letters? (Y/N)')     # Upper or lower case
    upper_case = input("> ")
    print('Include lowercase letters? (Y/N)')
    lower_case = input("> ")

    if upper_case.upper() == 'N' and lower_case.upper() == 'N':
        print('Please select any one of the upper case or lower case')
    elif upper_case.upper() == 'Y' and lower_case.upper() == 'Y':
        alphabets = alphabets_upper + alphabets_lower
        random_password.append(random.choice(alphabets_lower))
        random_password.append(random.choice(alphabets_upper))
        break
    elif upper_case.upper() == 'Y':
        alphabets = alphabets_upper
        random_password.append(random.choice(alphabets_upper))
        break
    elif lower_case.upper() == 'Y':
        alphabets = alphabets_lower
        random_password.append(random.choice(alphabets_lower))
        break

print('Include numbers? (Y/N)')              # Numbers
numbers = input("> ")
print('Include special characters? (Y/N)')   # Special characters
special_chracters = input("> ")

# Raw password
if numbers.upper() == "Y" and special_chracters.upper() == "Y":
    password = alphabets + num + s_ch
    random_password.append(random.choice(num))
    random_password.append(random.choice(s_ch))
elif numbers.upper() == "Y":
    password = alphabets + num
    random_password.append(random.choice(num))
elif special_chracters.upper() == "Y":
    password = alphabets + s_ch
    random_password.append(random.choice(s_ch))

# Random password
i=1
pre_lenght = len(random_password)
while i <= password_length-pre_lenght:
    random_password.append(random.choice(password))
    i+=1
random.shuffle(random_password)
print(f'The generated password is {''.join(random_password)}')