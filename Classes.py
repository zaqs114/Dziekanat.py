class Person:

    def __init__(self, firstname, lastname, pesel):
        self.firstname = firstname
        self.lastname = lastname
        self.pesel = pesel

    def __str__(self):
        return "Imie: " + self.firstname + " Nazwisko: " + self.lastname + " Pesel: " + self.pesel


class Student(Person):

    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel)
        self.studentID = studentID

    def __str__(self):
        return super().__str__() + " Numer indeksu: " + self.studentID


class Employee(Person):

    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel)
        self.salary = salary

    def __str__(self):
        return super().__str__() + " Wynagrodzenie: " + self.salary


class ITEmployee(Employee):

    itEmployeeList = []

    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel, salary)

    def __str__(self):
        return super().__str__()


class MathEmployee(Employee):

    mathEmployeeList = []

    def __init__(self, firstname, lastname, pesel, salary):
        super().__init__(firstname, lastname, pesel, salary)

    def __str__(self):
        return super().__str__()


class DailyStudent(Student):

    dailyStudentList = []

    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel, studentID)

    def __str__(self):
        return super().__str__()


class WeekendStudent(Student):

    weekendStudentList = []

    def __init__(self, firstname, lastname, pesel, studentID):
        super().__init__(firstname, lastname, pesel, studentID)

    def __str__(self):
        return super().__str__()


class Subjects:

    subjectList = []

    def __init__(self, subjectName, subjectID):
        self.subjectName=subjectName
        self.subjectID = subjectID

    def __str__(self):
        return "Nazwa przedmiotu: " + self.subjectName + " Oznaczenie przedmiotu: " + self.subjectID


class SubjectGroups:

    subjectGroupsList = []

    def __init__(self, subjectGroupName, subjectGroupID, studiesType, teacherName, nameOfStudents):
        self.subjectGroupName = subjectGroupName
        self.subjectGroupID = subjectGroupID
        self.studiesType = studiesType
        self.teacherName = teacherName
        self.nameOfStudents = nameOfStudents

    def __str__(self):
        return "Nazwa grupy przedmiotowej: " + self.subjectGroupName + " Oznaczenie grupy przedmiotowej: " + self.subjectGroupID + " Rodzaj studiow: " + self.studiesType + " Imie i nazwisko prowadzącego: " + self.teacherName + " Imiona i nazwiska studentów: " + self.nameOfStudents
