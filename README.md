# Academic Tracker and Planner - PyPulse

## 1. Project Overview

Academic Tracker and Study Planner is a simple Python-based console application designed to help students manage their academic activities in one place.

The application allows students to track subject progress, enter exam marks, manage events and deadlines, create to-do tasks, plan study activities, and view basic performance insights.

The project is developed using basic Python programming concepts such as functions, dictionaries, lists, loops, conditional statements, input/output, and modular programming.

---

## 2. Features

The application provides the following features:

### 1. Syllabus and Progress
- Allows the user to enter subjects.
- Allows the user to enter the progress percentage for each subject.
- Displays the progress of the entered subjects.

### 2. Exams and Results
- Allows the user to enter a subject name.
- Takes marks obtained and total marks.
- Calculates and displays the percentage.

### 3. Calendar and Events
- Allows the user to enter and manage academic events.

### 4. To-Do
- Allows the user to create and manage academic tasks.

### 5. Study Planner
- Helps the user enter and organize study planning information.

### 6. Deadline Tracker
- Allows the user to record and manage academic deadlines.

### 7. Performance Insight
- Uses the subject progress entered by the user.
- Provides a simple performance status based on the progress percentage.

### Main Menu
The application provides a menu-driven interface through which the user can select any of the available features or exit the program.

---

## 3. Technologies Used

- Python 3
- PyCharm
- Git and GitHub
- Python standard programming features and data structures

No external libraries are required for the current version of the project.

---

## 4. Project Structure

```text
Pycharm_Academic_planner/
│
├── README.md
│
└── src/
    ├── main.py
    ├── progress.py
    ├── grades.py
    ├── events.py
    ├── todo.py
    ├── study_planner.py
    ├── deadlines.py
    └── insights.py

Description of Source Files

main.py - Contains the main menu and connects the different modules.

progress.py - Handles subject progress tracking.

grades.py - Handles marks and percentage calculation.

events.py - Handles academic events.

todo.py - Handles to-do tasks.

study_planner.py - Handles study planning.

deadlines.py - Handles deadline tracking.

insights.py - Generates basic performance insights from subject progress.
```
## 5. Requirements

### 5.1 Software Requirements

- Python 3.x
- PyCharm or another Python-compatible IDE

### 5.2 Additional Requirements

- No additional Python packages are required.
- The project uses standard Python features and modules.


## 6. How to Run

### 6.1 Using PyCharm

1. Open the project in PyCharm.
2. Open the `src` folder.
3. Open `main.py`.
4. Run `main.py`.
5. Select an option from the main menu.
6. Enter the required information when prompted.

### 6.2 Using Command Line

1. Open a terminal in the project folder.
2. Run the following command: python src/main.py
3. The main menu will appear.
4. Select the required feature.

## 7. Testing
### 7.1 Testing Method
The project was tested using manual functional testing.
Each feature was run individually through the main menu.
### 7.2 Test Cases
Select menu options 1 to 7.
Enter valid inputs for each feature.
Check whether the expected output is displayed.
Select option 8 and check whether the program exits correctly.
Enter an invalid menu option and check the displayed response.
Test Performance Insight after entering subject progress.
Test percentage calculation using different marks and total marks.
### 7.3 Module Testing
The individual Python modules were tested after being connected to main.py.
The complete application was tested through the main menu.

## 8. Input and Output
### 8.1 Input

The user provides information such as:

Subject names,
Subject progress percentages,
Marks obtained,
Total marks,
Tasks,
Events,
Study plans,
Deadlines.
### 8.2 Output

The application displays:

Subject progress,
Calculated percentages,
Entered academic information,
Performance insights,
Menu options,
Status messages.

## 9. Limitations

The current version is a beginner-level console application.

Data is entered by the user during program execution.
The application does not use a database.
The application does not have a graphical user interface.
Data is not permanently stored after the program is closed.

## 10. Future Enhancements

Possible future improvements include:

Permanent storage of academic data using files or a database.
A graphical user interface.
More detailed academic reports.
Improved input validation.
Notifications or reminders for deadlines.
More detailed performance analysis.
Improved calendar and scheduling functionality.
 
## 11. Conclusion

Academic Tracker and Study Planner provides a simple way for students to organize common academic activities through a single Python-based application.

The project demonstrates the use of Python fundamentals, functions, data structures, conditional statements, loops, input/output, and modular programming to solve a practical academic management problem.
```