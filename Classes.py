class Person:

    def __init__(self, firstname, lastname, pesel):
        self.firstname = firstname
        self.lastname = lastname
        self.pesel = pesel

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.pesel


class Student(Person):

    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel)
        self.studentID = studentID

    def __str__(self):
        return super().__str__() + " " + self.studentID


class Employee(Person):

    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel)
        self.studentID = salary

    def __str__(self):
        return super().__str__() + " " + self.salary


class ITEmployee(Employee):
    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel, salary)

    def __str__(self):
        return super().__str__()


class MathEmployee(Employee):
    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel, salary)

    def __str__(self):
        return super().__str__()


class DailyStudent(Student):
    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel, studentID)

    def __str__(self):
        return super().__str__()


class WeekendStudent(Student):
    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel, studentID)

    def __str__(self):
        return super().__str__()


class Subjects:
    def __init__(self, subjectName, subjectID):
        self.subjectName=subjectName
        self.subjectID = subjectID

    def __str__(self):
        return self.subjectName + " " + self.subjectID


class SubjectGroups:
    def __init__(self, subjectGroupName, subjectGroupID, studiesType, teacherName, nameOfStudents):
        self.subjectGroupName = subjectGroupName
        self.subjectGroupID = subjectGroupID
        self.studiesType = studiesType
        self.teacherName = teacherName
        self.nameOfStudents = nameOfStudents

    def __str__(self):
        return self.subjectGroupName + " " + self.subjectGroupID + " " + self.studiesType + " " + self.teacherName + " " + self.nameOfStudents

z = DailyStudent("test", "kappa", "123", "2435")
print(z)