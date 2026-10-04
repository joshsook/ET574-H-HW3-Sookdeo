# List of student names
students = ["Jon", "Kim", "Lee", "Sara", "Miko",
            "Lin", "Toby", "Ben", "Mark", "Xia"]

# List of GPAs
gpas = [3.25, 2.25, 2.30, 4.00, 1.90,
        2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate the average GPA
total = sum(gpas)
average = total / len(gpas)

print("Average GPA:", round(average, 2))

print("\nStudents above the average:")

# Print students whose GPA is above the average
for i in range(len(students)):
    if gpas[i] > average:
        print(students[i], gpas[i])

# Predict scholarships
print("\nScholarship predictions:")

# Based on the examples, the lowest scholarship GPA is 2.75.
# Students with a GPA of 2.75 or higher are predicted
# to earn a scholarship.
for i in range(len(students)):
    if gpas[i] >= 2.75:
        print(students[i], gpas[i], "will earn a scholarship.")
