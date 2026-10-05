import csv

# Create an empty dictionary to store the students.
# Each student will have a major and GPA.
students = {}

# Open the CSV file and read the student information.
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        major = row["Major"]
        gpa = float(row["GPA"])

        # Store the information in the dictionary.
        students[name] = {
            "major": major,
            "gpa": gpa
        }

# Calculate the total of all GPAs.
total_gpa = 0

for name in students:
    total_gpa = total_gpa + students[name]["gpa"]

# Calculate the average GPA.
average_gpa = total_gpa / len(students)

print("Student Information")
print("-------------------")

for name in students:
    print(
        name,
        "-",
        students[name]["major"],
        "- GPA:",
        students[name]["gpa"]
    )

print()
print("Average GPA:", round(average_gpa, 2))

# Print students whose GPA is above the average.
print()
print("Students Above Average")
print("----------------------")

for name in students:
    if students[name]["gpa"] > average_gpa:
        print(name, "-", students[name]["gpa"])

# Predict scholarships using the examples.
#
# From the examples:
# Teri: 3.15 Math -> No
# Sue: 2.75 Biology -> Yes
# Markus: above average Biology -> Yes
# Anders: above average Math -> No
# Leigh: 3.57 Math -> Yes
# Jon: 3.67 Math -> Yes
#
# The examples suggest that:
# - Biology students with a GPA of 2.75 or higher earn a scholarship.
# - Math students need a GPA of at least 3.57.
# - For Computer Science, we will use 3.50 as the predicted cutoff.
#
# These are predictions based only on the examples,
# not an actual scholarship policy.

print()
print("Predicted Scholarship Winners")
print("-----------------------------")

for name in students:
    major = students[name]["major"]
    gpa = students[name]["gpa"]

    scholarship = False

    if major == "Biology" and gpa >= 2.75:
        scholarship = True

    if major == "Math" and gpa >= 3.57:
        scholarship = True

    if major == "Computer Science" and gpa >= 3.50:
        scholarship = True

    if scholarship:
        print(name, "-", major, "-", gpa, "- Scholarship: YES")
    else:
        print(name, "-", major, "-", gpa, "- Scholarship: NO")
