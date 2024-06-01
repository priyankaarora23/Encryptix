import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789<>:?+{-}][]"
length = int(input("Enter the desired length of your password: "))
password = ""

for i in range(length):
    password += random.choice(chars)
print(password)
