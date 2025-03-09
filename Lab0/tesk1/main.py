class Student:
    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = {}

    def add_grade(self, subject, grade):
        self.subjects[subject] = grade

    def __str__(self):
        result = f"Student: {self.name} {self.surname}\n"
        for subject, grade in self.subjects.items():
            result += f"----{subject}: {grade}\n"
        return result


def calculate_grade(total_points):
    if total_points <= 50:
        return 5
    elif total_points <= 60:
        return 6
    elif total_points <= 70:
        return 7
    elif total_points <= 80:
        return 8
    elif total_points <= 90:
        return 9
    else:
        return 10


def main():
    students = {}

    while True:
        line = input().strip()
        if line == "end":
            break
        name, surname, index, subject, theory_points, practical_points, lab_points = line.split(",")
        theory_points = float(theory_points)
        practical_points = float(practical_points)
        lab_points = float(lab_points)
        total_points = theory_points + practical_points + lab_points
        grade = calculate_grade(total_points)

        if index not in students:
            students[index] = Student(name, surname, index)

        students[index].add_grade(subject, grade)

    for student in students.values():
        print(student)


if __name__ == "__main__":
    main()

# def calculate_grade(total_points):
#     if total_points <= 50:
#         return 5
#     elif total_points <= 60:
#         return 6
#     elif total_points <= 70:
#         return 7
#     elif total_points <= 80:
#         return 8
#     elif total_points <= 90:
#         return 9
#     else:
#         return 10
#
#
# def main():
#     students = {}
#
#     while True:
#         line = input().strip()
#         if line == "end":
#             break
#         name, surname, index, subject, theory_points, practical_points, lab_points = line.split(",")
#         theory_points = float(theory_points)
#         practical_points = float(practical_points)
#         lab_points = float(lab_points)
#         total_points = theory_points + practical_points + lab_points
#         grade = calculate_grade(total_points)
#
#         if index not in students:
#             students[index] = {
#                 "name": name,
#                 "surname": surname,
#                 "subjects": {}
#             }
#
#         students[index]["subjects"][subject] = grade
#
#     for index, info in students.items():
#         print(f"Student: {info['name']} {info['surname']}")
#         for subject, grade in info["subjects"].items():
#             print(f"----{subject}: {grade}")
#         print()
#
#
#
# if __name__ == "__main__":
#     main()
#
