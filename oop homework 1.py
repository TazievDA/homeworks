class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __avg_grade(self):
        grades_list = []
        for course in self.courses_in_progress:
            grade = self.grades.get(course)
            grades_list.extend(grade)
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__avg_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __gt__(self, other):
        return self.__avg_grade() > other.__avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
        lecturers_list.append(self)

    def __avg_grade(self):
        grades_list = []
        for course in self.courses_attached:
            grade = self.grades.get(course)
            grades_list.extend(grade)
        return sum(grades_list) / len(grades_list)

    def __gt__(self, other):
        return self.__avg_grade() > other.__avg_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__avg_grade()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def manual_avg_students_grade(students):
    course = input('Введите название курса для расчёта среднего балла по всем студентам: ').capitalize()
    all_grades = []
    for student in students_list:
        if course in student.courses_in_progress:
            all_grades.extend(student.grades[course])
        else:
            return f'Ошибка. Курс "{course}" не найден.'
    return f'Средняя оценка за домашние задания на курсе "{course}": {round(sum(all_grades) / len(all_grades), 2)}'


def manual_avg_lecturers_grade(lecturers):
    course = input('Введите название курса для расчёта среднего балла по всем лекторам: ').capitalize()
    all_grades = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            all_grades.extend(lecturer.grades[course])
        else:
            return f'Ошибка. Курс "{course}" не найден.'
    return f'Средняя оценка за лекции на курсе "{course}": {round(sum(all_grades) / len(all_grades), 2)}'

# Список студентов для вычисления средней оценки за домашние работы.
students_list = []

# Список лекторов для вычисления средней оценки за лекции.
lecturers_list = []

# Создание экземпляров.

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']


bad_student = Student('Vasya', 'Pupkin', 'male')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Java']
bad_student.finished_courses += ['Введение в программирование']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['Java']

lecturer2 = Lecturer('Another', 'Buddy')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Java']

reviewer = Reviewer('Yet Another', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Java']

reviewer2 = Reviewer('One more', 'Buddy')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

# Проверка работоспособности методов.

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(bad_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 5)
reviewer.rate_hw(bad_student, 'Java', 5)
reviewer.rate_hw(best_student, 'Java', 1)

reviewer2.rate_hw(best_student, 'Python', 2)
reviewer2.rate_hw(bad_student, 'Python', 2)
reviewer2.rate_hw(best_student, 'Python', 2)
reviewer2.rate_hw(bad_student, 'Java', 2)
reviewer2.rate_hw(best_student, 'Java', 1)

best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Java', 5)
best_student.rate_lecturer(lecturer, 'Java', 6)

best_student.rate_lecturer(lecturer2, 'Python', 1)
best_student.rate_lecturer(lecturer2, 'Python', 1)
best_student.rate_lecturer(lecturer2, 'Python', 1)
best_student.rate_lecturer(lecturer2, 'Java', 1)
best_student.rate_lecturer(lecturer2, 'Java', 1)
best_student.rate_lecturer(lecturer2, 'Java', 2)

print(reviewer)
print()
print(lecturer)
print()
print(best_student)
print()
print(bad_student)
print()
print(best_student < bad_student)
print()
print(lecturer > lecturer2)
print()
print(manual_avg_students_grade(students_list))
print()
print(manual_avg_lecturers_grade(lecturers_list))