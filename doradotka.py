class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecture_grade = {}


    def _average_s(self):
        number = sum(list(self.lecture_grade.values()),[])
        return sum(number) / len(number)


    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self._average_s()}"""


class Lecturer_1(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecture_grade_1 = {}


    def _average_s(self):
        number = sum(list(self.lecture_grade_1.values()),[])
        return sum(number) / len(number)


    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self._average_s()}"""


    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self._average_s() > other._average_s():
                return f'Лучший лектор на курсе: {self.name} {self.surname}'
            else:
                return f'Лучший лектор на курсе: {other.name} {other.surname}'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}"""


class Reviewer_1(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student_1) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}"""


class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate(self, lecturer, course, lecture_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grade:
                lecturer.lecture_grade[course] += [lecture_grade]
            else:
                lecturer.lecture_grade[course] = [lecture_grade]
        else:
            return 'Ошибка'


    def _average_st(self):
        number = sum(list(self.grades.values()),[])
        return sum(number) / len(number)


    def _average_py(self):
        key_py = self.grades.get('Python')
        return sum(key_py) / len(key_py)


    def _average_git(self):
        key_git = self.grades.get('Git')
        return sum(key_git) / len(key_git)


    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self._average_st()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}"""


class Student_1():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate(self, lecturer, course, lecture_grade):
        if isinstance(lecturer, Lecturer_1) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grade_1:
                lecturer.lecture_grade_1[course] += [lecture_grade]
            else:
                lecturer.lecture_grade_1[course] = [lecture_grade]
        else:
            return 'Ошибка'


    def _average_st(self):
        number = sum(list(self.grades.values()),[])
        return sum(number) / len(number)


    def _average_py(self):
        key_py = self.grades.get('Python')
        return sum(key_py) / len(key_py)


    def _average_git(self):
        key_git = self.grades.get('Git')
        return sum(key_git) / len(key_git)


    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self._average_st()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        """

    def __gt__(self, other):
        if isinstance(other, Student):
            if self._average_st() > other._average_st():
                return f'Лучший показатель в обучении: {self.name} {self.surname}'
            else:
                return f'Лучший показатель в обучении: {other.name} {other.surname}'



some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']


some_lecturer_1 = Lecturer_1('Bill', 'Hawkins')
some_lecturer_1.courses_attached += ['Python', 'Git']


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']


some_reviewer_1 = Reviewer_1('Bill', 'Hawkins')
some_reviewer_1.courses_attached += ['Python', 'Git']


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в програмирование']


some_student_1 = Student_1('Otto', 'Schmidt', 'men')
some_student_1.courses_in_progress += ['Python', 'Git']
some_student_1.finished_courses += ['Введение в програмирование']


some_student.rate(some_lecturer, 'Python', 10)
some_student.rate(some_lecturer, 'Python', 10)
some_student.rate(some_lecturer, 'Python', 10)
some_student.rate(some_lecturer, 'Python', 10)
some_student.rate(some_lecturer, 'Git', 9)
some_student.rate(some_lecturer, 'Git', 10)
some_student.rate(some_lecturer, 'Python', 10)
some_student.rate(some_lecturer, 'Git', 10)
some_student.rate(some_lecturer, 'Git', 10)
some_student.rate(some_lecturer, 'Git', 10)


some_student_1.rate(some_lecturer_1, 'Python', 10)
some_student_1.rate(some_lecturer_1, 'Python', 10)
some_student_1.rate(some_lecturer_1, 'Python', 10)
some_student_1.rate(some_lecturer_1, 'Python', 9)
some_student_1.rate(some_lecturer_1, 'Git', 10)
some_student_1.rate(some_lecturer_1, 'Git', 10)
some_student_1.rate(some_lecturer_1, 'Python', 9)
some_student_1.rate(some_lecturer_1, 'Git', 10)
some_student_1.rate(some_lecturer_1, 'Git', 10)
some_student_1.rate(some_lecturer_1, 'Git', 10)


some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)


some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_1, 'Git', 10)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)
some_reviewer_1.rate_hw(some_student_1, 'Git', 10)
some_reviewer_1.rate_hw(some_student_1, 'Git', 10)
some_reviewer_1.rate_hw(some_student_1, 'Git', 9)






print(some_reviewer_1)
print(some_reviewer)
print(some_lecturer_1)
print(some_lecturer)
print('_________________________')
print(some_lecturer_1 > some_lecturer)
print('_________________________')
print(some_student_1)
print(some_student)
print("__________________")
print(some_student_1 > some_student)
print('__________________')
