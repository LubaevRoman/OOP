
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        count_grade = 0
        for k in self.grades:
            count_grade += len(self.grades[k])
        self.average_grade = sum(map(sum, self.grades.values())) / count_grade
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_grade}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы" {self.finished_courses}'''
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average_grade == other.average_grade

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_value = float()
        self.grades = {}

    def __str__(self) -> str:
        count_grade = 0
        for v in self.grades:
            count_grade += len(self.grades[v])
        self.average_value = sum(map(sum, self.grades.values())) / count_grade
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_value}'''
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это не Лектор!'
        return self.average_value == other.average_value

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        result = f'''Имя: {self.name}
        Фамилия: {self.surname}'''
        return result

#------------------------------------
lecturer_1 = Lecturer('Rinat', 'Ganiev')
lecturer_1.courses_attached += ['Python, Git']
lecturer_2 = Lecturer('Alexandr', 'Masharov')
lecturer_2.courses_attached += ['Python, Git']
#------------------------------------
student_1 = Student('Roman', 'Lubaev', 'Male')
student_1.courses_in_progress += ['Python, Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Liana', 'Fatkullina', 'Female')
student_2.courses_in_progress += ['Python, Git']
student_2.finished_courses += ['Введение в программирование']
#------------------------------------
reviewer_1 = Reviewer('Tagir', 'Kolenko')
reviewer_1.courses_attached += ['Python, Git']
reviewer_2 = Reviewer('Juri', 'Harkin')
reviewer_2.courses_attached += ['Python, Git']
#------------------------------------

student_1.rate_lecture(lecturer_1, 'Python, Git', 10)
student_1.rate_lecture(lecturer_2, 'Python, Git', 8)
student_2.rate_lecture(lecturer_1, 'Python, Git', 8)
student_2.rate_lecture(lecturer_2, 'Python, Git', 10)

reviewer_1.rate_hw(student_1, 'Python, Git', 9)
reviewer_1.rate_hw(student_2, 'Python, Git', 10)
reviewer_2.rate_hw(student_1, 'Python, Git', 10)
reviewer_2.rate_hw(student_2, 'Python, Git', 9)

print()
print(f'''Список проверяющих:
      {reviewer_1}, 
      {reviewer_2} ''')
print('___________________________')
print(f'''Список лекторов:
      {lecturer_1}, 
      {lecturer_2} ''')
print(lecturer_1.__lt__(lecturer_2))
print('___________________________')
print(f'''Список студентов:
      {student_1}, 
      {student_2} ''')
print(student_1.__lt__(student_2))
print('---------------------------')

student_list = [student_1, student_2]

def average_all_student(student_list, course_name):
    sum_all_stud = 0
    count_all_stud = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            sum_all_stud += student.average_grade
            count_all_stud += 1
    averge_all = sum_all_stud / count_all_stud
    return float(averge_all)

print(
    f"Cредняя оценка за домашние задание по всем студентам в рамках курса {'Python, Git'}: {average_all_student(student_list, 'Python, Git')}")

lecturer_lsit = [lecturer_1, lecturer_2]

def average_all_lecturer(lecturer_list, course_name):
    sum_all_lect = 0
    count_all_lect = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course_name]:
            sum_all_lect += lecturer.average_value
            count_all_lect += 1
    average_all_lect = sum_all_lect / count_all_lect
    return float(average_all_lect)

print(
    f"Средняя оценка за лекции всех лекторов в рамках курса {'Python, Git'}: {average_all_lecturer(lecturer_lsit, 'Python, Git')}")
print('---------------------------')

