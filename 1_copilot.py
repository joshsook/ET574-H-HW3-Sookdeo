# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
# add more students after the list is created
students.append("Sara")
students.append("Miko")

# function to print 'Hi name' for each student in the list and total count
def print_greetings(student_list):
    print(f"Total students: {len(student_list)}")
    for name in student_list:
        print(f"Hi {name}")

# change Jon to John
students[0] = 'John'
# call the function
print_greetings(students)
