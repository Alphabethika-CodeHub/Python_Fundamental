class Student:
    def __init__(self, name, task_scores):
        self.name = name
        self.task_scores = task_scores

    def average_score(self):
        return sum(self.task_scores) / len(self.task_scores)

    def is_passed(self):
        return self.average_score() >= 75

    def display_tasks(self):
        return " | ".join(f"T{idx+1}:score" for idx, score in enumerate(self.task_scores))
