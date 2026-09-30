from progress import subject_progress_tracker
from grades import grade_calculator
from events import event_tracker
from todo import todo_tracker
from study_planner import study_planner
from deadlines import deadline_tracker
from insights import performance_insights

subject_progress = {}
while True:
    print("--- STUDENT DASHBOARD ---")
    print("1. Syllabus and Progress")
    print("2. Exams and Results ")
    print("3. Calendar and Events")
    print("4. To-Do")
    print("5. Study Planner")
    print("6. Deadline Tracker")
    print("7. Performance Insight")
    print("8. Exit")

    choice = input("entre your choice:")
    if choice == "1":
        subject_progress = subject_progress_tracker()
    elif choice == "2":
        grade_calculator()
    elif choice == "3":
        event_tracker()
    elif choice == "4":
        todo_tracker()
    elif choice == "5":
        study_planner()
    elif choice == "6":
        deadline_tracker()
    elif choice == "7":
        performance_insights(subject_progress)
    elif choice == "8":
        print("exiting program")
        break
    else:
        print("invaild choice, please try again")