def grade_calculator():
    total_sub = int(input("number of subject:"))
    for i in range(total_sub):
        subject = input("name of subject:")
        marks = int(input("marks obtained:"))
        total_marks = int(input("total marks="))
        percentage = (marks / total_marks) * 100
        print(percentage)
