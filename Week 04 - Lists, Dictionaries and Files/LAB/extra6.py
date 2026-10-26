
name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favourite color: ")

with open("my_profile.txt", "w") as file:
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(color + "\n")

with open("my_profile.txt", "r") as file:
    lines = file.readlines()

print("Name:", lines[0].strip())
print("Age:", lines[1].strip())
print("Favorite Color:", lines[2].strip())
