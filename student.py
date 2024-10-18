class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            print(f"Invalid grade for {subject}. Must be between 0 and 100.")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

    def display_student_info(self):
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "grades": self.grades,
            "average": self.calculate_average()
        }
class StudentTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number not in self.students:
            self.students[roll_number] = Student(name, roll_number)
        else:
            print(f"Student with roll number {roll_number} already exists.")

    def add_grade(self, roll_number, subject, grade):
        if roll_number in self.students:
            self.students[roll_number].add_grade(subject, grade)
        else:
            print(f"No student found with roll number {roll_number}.")

    def view_student_details(self, roll_number):
        if roll_number in self.students:
            return self.students[roll_number].display_student_info()
        else:
            return f"No student found with roll number {roll_number}."

    def calculate_average(self, roll_number):
        if roll_number in self.students:
            return self.students[roll_number].calculate_average()
        else:
            return f"No student found with roll number {roll_number}."
tracker = StudentTracker()

while True:
    print("\n1. Add Student\n2. Add Grade\n3. View Student Details\n4. Calculate Average\n5. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        tracker.add_student(name, roll_number)
    elif choice == 2:
        roll_number = input("Enter roll number: ")
        subject = input("Enter subject: ")
        grade = int(input("Enter grade: "))
        tracker.add_grade(roll_number, subject, grade)
    elif choice == 3:
        roll_number = input("Enter roll number: ")
        print(tracker.view_student_details(roll_number))
    elif choice == 4:
        roll_number = input("Enter roll number: ")
        print(f"Average: {tracker.calculate_average(roll_number)}")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
from flask import Flask, request, render_template

app = Flask(__name__)
tracker = StudentTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_number = request.form['roll_number']
    tracker.add_student(name, roll_number)
    return "Student added successfully!"

@app.route('/add_grade', methods=['POST'])
def add_grade():
    roll_number = request.form['roll_number']
    subject = request.form['subject']
    grade = int(request.form['grade'])
    tracker.add_grade(roll_number, subject, grade)
    return "Grade added successfully!"

@app.route('/view_student', methods=['GET'])
def view_student():
    roll_number = request.args.get('roll_number')
    return tracker.view_student_details(roll_number)

@app.route('/calculate_average', methods=['GET'])
def calculate_average():
    roll_number = request.args.get('roll_number')
    return f"Average: {tracker.calculate_average(roll_number)}"

if __name__ == '__main__':
    app.run(debug=True)
