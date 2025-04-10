from mini_projects.student_grader.models.student import Student


class GradeSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, task_scores):
        self.students.append(Student(name, task_scores))

    def show_all_student(self):
        print("Student List And Scores")
        for student in self.students:
            print(f"{student.name}: {student.display_tasks()}")

    def show_passed_students(self):
        print("Passed Students")
        for student in self.students:
            if student.is_passed():
                print(f"{student.name} - Avg: {round(student.average_score(), 2)}")

    def show_averages(self):
        print("\n Average Score Summary")
        for student in self.students:
            print(f"{student.name}: {round(student.average_score(), 2)}")

    def recheck_score(self):
        print("\n Recheck Student Score (Max 3 Attemps)")
        attempt = 0
        while attempt < 3:
            name = input("Enter Student Name: ")
            student = self.find_student(name)
            if not student:
                print("Student Not Found!")
                attempt += 1
                continue
            print(f"{student.name}'s Scores: {student.task_scores}")
            if not student.is_passed():
                print("Suggest: Retake Exam.")
            break

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

