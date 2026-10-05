# Store each student's major and GPA in a dictionary
students = {
    "Jon": {"GPA": 3.25, "major": "Math"},
    "Kim": {"GPA": 2.25, "major": "Biology"},
    "Lee": {"GPA": 2.30, "major": "Math"},
    "Sara": {"GPA": 4.00, "major": "Math"},
    "Miko": {"GPA": 1.90, "major": "Math"},
    "Lin": {"GPA": 2.10, "major": "Biology"},
    "Toby": {"GPA": 2.89, "major": "Biology"},
    "Ben": {"GPA": 2.75, "major": "Math"},
    "Mark": {"GPA": 2.34, "major": "Math"},
    "Xia": {"GPA": 3.53, "major": "Biology"}
}

# Add all of the GPAs together
total_gpa = 0

for student in students:
    total_gpa = total_gpa + students[student]["GPA"]

# Calculate the average GPA
average_gpa = total_gpa / len(students)

print("Average GPA:", round(average_gpa, 2))

# Print students whose GPA is above the average
print("\nStudents above average:")

for student in students:
    if students[student]["GPA"] > average_gpa:
        print(student, students[student]["GPA"], students[student]["major"])

# Predict scholarships
print("\nScholarship predictions:")

for student in students:
    gpa = students[student]["GPA"]
    major = students[student]["major"]

    # Prediction based on the examples:
    # Biology students with GPA 2.75 or higher earn a scholarship.
    # Math students need a GPA above the average AND a GPA of at least 3.50.

    if major == "Biology" and gpa >= 2.75:
        scholarship = "Yes"
    elif major == "Math" and gpa >= 3.50:
        scholarship = "Yes"
    else:
        scholarship = "No"

    print(student, "-", scholarship)
