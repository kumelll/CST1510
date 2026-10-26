
marks = [78, 45, 89, 56, 32, 95, 67]

average = sum(marks) / len(marks)
passed = 0
failed = 0

for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print("Average:", round(average, 2))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Passed:", passed)
print("Failed:", failed)
