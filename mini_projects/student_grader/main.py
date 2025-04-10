from mini_projects.student_grader.core.grade_system import GradeSystem


def main():
    system = GradeSystem()

    # Entry Data
    system.add_student("Daffa", [80, 85, 90])
    system.add_student("Adit", [60, 40, 50])
    system.add_student("Nisa", [70, 72, 75])
    system.add_student("Rina", [88, 90, 95])

    # Jalankan Fitur
    system.show_all_student()
    system.show_passed_students()
    system.recheck_score()
    system.show_averages()

if __name__ == "__main__":
    main()