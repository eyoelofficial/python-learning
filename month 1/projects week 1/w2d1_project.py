import secrets
import string
lenght = int(input("password lenghth: "))
characters = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)
password = ""
for _ in range(lenght):
    password += secrets.choice(characters)
print("password: ",password)