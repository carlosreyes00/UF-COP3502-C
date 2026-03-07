from course_data import actual_data

student_name = input("Enter the student's name: ")

data = actual_data

if student_name not in data["roster"]:
    print("Student not found.")
else:
    total = 0

    for assignment_name, assignment_data in data["assignments"].items():
        weight = assignment_data["weight"]
        submissions = assignment_data["submissions"]

        score = submissions.get(student_name, 0)

        print(f"{assignment_name}: {score}%")

        total += score * (weight / 100)

    print(f"Total grade: {total:.2f}%")