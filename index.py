import random
import string
def generate_password(length):
   lowercase = string.ascii_lowercase
   uppercase = string.ascii_uppercase
   digits = string.digits
   characters = lowercase + uppercase + digits
   password=''.join(random.choice(characters) for _ in range(length))
   return password
password_length=int(input("enter the desired password length :"))
password = generate_password(password_length)
print("Your password is:",password)
