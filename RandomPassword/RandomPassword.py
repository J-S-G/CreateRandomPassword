#Objective: Import the module: random - pseudo-random number generators
import random as r
import string as s
#list(string.ascii_uppercase) = alphabet characters (26) 
upper_char = list(s.ascii_uppercase)
lower_char = list(s.ascii_lowercase)
number = ['1', '2', '3', '4', '5']
special_char = ['!', '@', '#', '$', '%', '&']

password = r.choice(upper_char) + r.choice(lower_char) + r.choice(number) + r.choice(special_char) + r.choice(upper_char) + r.choice(lower_char) + r.choice(number) + r.choice(special_char) 
print(password)