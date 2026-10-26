
import random
import string

letters = list(string.ascii_letters)
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)
print("Your password is:", password)
