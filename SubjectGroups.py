import Classes
import os


def subject_groups_menu():
    choice = input("""Grupy przediotowe.
                Wybierz 0 aby powrócić do poprzedniego menu.
                Wybierz 1 aby dodać grupe przedmiotową.
                Wybierz 2 aby usunąć grupę przedmiotową.
                """)
    if choice == "0":
        os.system('cls')
        import Main
        Main.edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_subject_group()

    if choice == "2":
        os.system('cls')
        delete_subject_group()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
            """)
        subject_groups_menu()


def add_subject_group():
    print("Dodawanie grupy przedmiotowej.")
    subjectGroupID=input("""Wprowadź oznaczenie grupy
    """)
    if not Classes.Subjects.subjectList:
        choice = input("""W bazie nie ma żadnego przedmiotu. Dodaj jakiś i spróbuj ponownie. Wybierz cokolwiek aby powrócić.
                    """)
        os.system('cls')
        subject_groups_menu()

    j = 1
    for i in Classes.Subjects.subjectList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz przedmiot dla którego chcesz utworzyć nową grupę..
                """))
    choice -= 1
    subjectGroupName = Classes.Subjects.subjectList[choice].subjectName
    print(subjectGroupName)
    os.system('cls')
    choice=int(input("""Dodawanie grupy przedmiotowej.
    Wybierz 1 aby dodać informatyka do grupy.
    Wybierz 2 aby dodać matematyka do grupy
    """))
    if choice==1:
        os.system('cls')
        teacherName=add_itemployee_to_group()
        choice = int(input("""Dodawanie grupy przedmiotowej.
                            Wybierz 1 aby studentów dziennych do grupy.
                            Wybierz 2 aby studentów zaocznych do grupy
                            """))
        if choice == 1:
            studentNames = []
            studentNames = add_daily_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append(
                Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Dzienne", teacherName, studentNames))

        if choice==2:
            studentNames = []
            studentNames = add_weekend_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append(Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Zaoczne", teacherName, studentNames))
    if choice == 2:
        os.system('cls')
        teacherName = add_mathemployee_to_group()
        choice = int(input("""Dodawanie grupy przedmiotowej.
                            Wybierz 1 aby dodać studentów dziennych do grupy.
                            Wybierz 2 aby dodać studentów zaocznych do grupy
                            """))
        if choice == 1:
            studentNames = []
            studentNames = add_daily_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append(
                Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Dzienne", teacherName, studentNames))


        if choice == 2:
            studentNames = []
            studentNames = add_weekend_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append(
                Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Zaoczne", teacherName, studentNames))
    os.system('cls')
    print("Pomyślnie dodano grupe przedmiotowa")
    print()
    add_subject_group()


def add_itemployee_to_group():
    if not Classes.ITEmployee.itEmployeeList:
        os.system('cls')
        print("W bazie nie ma żadnych pracowników. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.ITEmployee.itEmployeeList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                        """))
    choice -= 1
    teacherName = Classes.ITEmployee.itEmployeeList[choice].firstname + " " + Classes.ITEmployee.itEmployeeList[choice].lastname
    print(teacherName)
    return teacherName


def add_mathemployee_to_group():
    if not Classes.MathEmployee.mathEmployeeList:
        os.system('cls')
        print("W bazie nie ma żadnych pracowników. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.MathEmployee.mathEmployeeListt:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                        """))
    choice -= 1
    teacherName = Classes.MathEmployee.mathEmployeeList[choice].firstname + " " + Classes.MathEmployee.mathEmployeeList[choice].lastname
    print(teacherName)
    return teacherName


def add_daily_student_to_group():
    if not Classes.DailyStudent.dailyStudentList:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.DailyStudent.dailyStudentList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                """))
    choice -= 1
    studentNames = []
    studentNames.append(Classes.DailyStudent.dailyStudentList[choice].name + Classes.DailyStudent.dailyStudentList[choice].surname )
    choice=int(input("""
    Wybierz 1 aby dodać kolejnego studenta.
    Wybierz cokolwiek aby powrócić"""))
    if choice == 1:
        add_daily_student_to_group()
    else:
        return studentNames


def add_weekend_student_to_group():
    if not Classes.WeekendStudent.weekendStudentList:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    j = 1
    for i in Classes.WeekendStudent.weekendStudentList:
        print(j, '. ', i)
        j += 1
    choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                   """))
    choice -= 1
    studentNames = []
    studentNames.append(Classes.WeekendStudent.weekendStudentList[choice].name +Classes.WeekendStudent.weekendStudentList[choice].surname)
    choice = int(input("""
       Wybierz 1 aby dodać kolejnego studenta.
       Wybierz 0 aby powrócić"""))
    if choice == 1:
        add_daily_student_to_group()
    else:
        return studentNames


def delete_subject_group():
    try:
        j = 1
        print("Usuwanie przedmiotu.")
        print()
        if not Classes.Subjects.subjectList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
                """)
            os.system('cls')
            subject_groups_menu()

        for i in Classes.Subjects.subjectList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
            """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.Subjects.subjectList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto przedmiot.")
        print()
        subject_groups_menu()
    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
            """)
        subject_groups_menu()
