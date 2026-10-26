
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

grades["Diana"] = 88
grades["Bob"] = 95

for name, score in grades.items():
    if score > 80:
        print(name, score)

average = sum(grades.values()) / len(grades)
print("Average score:", round(average, 2))
