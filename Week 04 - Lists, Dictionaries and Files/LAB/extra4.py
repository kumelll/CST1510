
student_data = [
    [101, "Alice", 85, 92, 88],
    [102, "Bob", 78, 81, 75],
    [103, "Charlie", 90, 85, 89],
    [104, "David", 65, 70, 72],
    [105, "Eve", 88, 95, 90]
]

for student in student_data:
    average = sum(student[2:5]) / 3
    student.append(average)

    print(student[1], "Average:", round(average, 2))

averages = [student[5] for student in student_data]

print("Highest average:", max(averages))
print("Lowest average:", min(averages))

print("Students above 75 in all subjects:")

for student in student_data:
    if all(mark > 75 for mark in student[2:5]):
        print(student[1])
