class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Mentor_1():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecture_grade = {}

    def __str__(self):
        nunber = sum(list(self.lecture_grade.values()),[])
        key_py = self.lecture_grade.get('Python')
        key_git = self.lecture_grade.get('Git')
        date = sum(nunber) / len(nunber)
        if date < 6.5:
            result = ('Качество обучения "плохо".')
        elif date < 8.7:
            result = ('Качество обучения "хорошо".')
        else:
            result = ('Качество обучения "отлично".')

        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {(sum(nunber) / len(nunber))}
        Средняя оценка лекции 'Python': {sum(key_py) / len(key_py)}
        Средняя оценка лекции 'Git': {sum(key_git) / len(key_git)}
        {result}"""
    

class Lecturer_1(Mentor_1):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lecture_grade = {}

    def __str__(self):
        nunber = sum(list(self.lecture_grade.values()),[])
        key_py = self.lecture_grade.get('Python')
        key_git = self.lecture_grade.get('Git')
        date = sum(nunber) / len(nunber)
        if date < 6.5:
            result = ('Качество обучения "плохо".')
        elif date < 8.7:
            result = ('Качество обучения "хорошо".')
        else:
            result = ('Качество обучения "отлично".')

        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {(sum(nunber) / len(nunber))}
        Средняя оценка лекции 'Python': {sum(key_py) / len(key_py)}
        Средняя оценка лекции 'Git': {sum(key_git) / len(key_git)}
        {result}"""
    
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
    

class Reviewer_1(Mentor_1):
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

    def __str__(self):
        number = sum(list(self.grades.values()),[])
        key_py = self.grades.get('Python')
        key_git = self.grades.get('Git')
        x = (self.courses_in_progress)
        date = sum(number) / len(number)
        if date < 6.5:
            result = ('Результат обучения "плохой", необходимо подтянуть знания.')
        elif date < 8.7:
            result = ('Результат обучения "хорошо", вы можете и лучше учиться.')
        else:
            result = ('Результат обучения "отлично", так держать!')

        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {sum(number) / len(number)}
        Курсы в процессе изучения: {x[0]}, {x[1]}
        Завершенные курсы: {self.finished_courses[0]}
        Среднняя оценка за Д/З по предмету 'Python': {sum(key_py) / len(key_py)}
        Среднняя оценка за Д/З по предмету 'Git' : {sum(key_git) / len(key_git)}
        {result}"""

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
            if course in lecturer.lecture_grade:
                lecturer.lecture_grade[course] += [lecture_grade]
            else:
                lecturer.lecture_grade[course] = [lecture_grade]
        else:
            return 'Ошибка'

    def __str__(self):
        number = sum(list(self.grades.values()),[])
        key_py = self.grades.get('Python')
        key_git = self.grades.get('Git')
        x = (self.courses_in_progress)
        date = sum(number) / len(number)
        if date < 6.5:
            result = ('Результат обучения "плохой", необходимо подтянуть знания.')
        elif date < 8.7:
            result = ('Результат обучения "хорошо", вы можете и лучше учиться.')
        else:
            result = ('Результат обучения "отлично", так держать!')

        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {sum(number) / len(number)}
        Курсы в процессе изучения: {x[0]}, {x[1]}
        Завершенные курсы: {self.finished_courses[0]}
        Среднняя оценка за Д/З по предмету 'Python': {sum(key_py) / len(key_py)}
        Среднняя оценка за Д/З по предмету 'Git' : {sum(key_git) / len(key_git)}
        {result}"""


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


# print(some_reviewer_1)
# print(some_reviewer)
print(some_lecturer_1)
print(some_lecturer)
print(some_student_1)
print(some_student)