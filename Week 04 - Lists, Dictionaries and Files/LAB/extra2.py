
import random

throws = []

for i in range(7):
    throws.append(random.randint(1, 6))

random.shuffle(throws)
print("Shuffled:", throws)

throws.sort(reverse=True)
print("Descending:", throws)

for num in range(1, 7):
    print(f"{num} appears {throws.count(num)} times")
