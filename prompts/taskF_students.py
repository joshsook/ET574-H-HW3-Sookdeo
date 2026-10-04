# Store student names and GPAs in two lists
students = ["Jon", "Kim", "Lee", "Sara", "Miko",
            "Lin", "Toby", "Ben", "Mark", "Xia"]

gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
        2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate the average GPA
total = sum(gpas)
average = total / len(gpas)

print("Average GPA:", round(average, 2))

# Print students above the average
print("\nStudents above average:")

for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], "-", gpas[i])

# Predict scholarship students
print("\nPredicted scholarship students (GPA 3.0 or higher):")

for i in range(len(students)):
    if gpas[i] >= 3.0:
        print(students[i], "-", gpas[i])
        