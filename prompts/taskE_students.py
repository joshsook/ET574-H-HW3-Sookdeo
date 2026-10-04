students = []
gpas = []

for i in range(25):
    name = input(f"Enter student {i + 1}'s name: ")
    gpa = float(input(f"Enter {name}'s GPA: "))

    students.append(name)
    gpas.append(gpa)

print("\nStudent Records:")
for i in range(25):
    print(f"{students[i]}: {gpas[i]:.2f}")

