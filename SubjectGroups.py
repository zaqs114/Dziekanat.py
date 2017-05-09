import Classes
import os


def subject_groups_menu():
    choice = input("""Grupy przediotowe.
                Wybierz 0 aby powrócić do poprzedniego menu.
                Wybierz 1 aby dodać grupe przedmiotową.
                Wybierz 2 aby usunąć grupę przedmiotową.
                """)
    if choice == "0":
        subject_group_write_to_file()
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
    subjectGroupName = Classes.Subjects.subjectList[choice].Classes.Subjects.return_subject_name()

    os.system('cls')
    choice=int(input("""Dodawanie grupy przedmiotowej.
    Wybierz 1 aby dodać informatyka do grupy.
    Wybierz 2 aby dodać matematyka do grupy
    """))
    if choice == "1":
        if not Classes.ITEmployee.itEmployeeList:
            os.system('cls')
            print("W bazie nie ma żadnych pracowników. Dodaj je, i spróbuj ponownie.")
            subject_groups_menu()
        j = 1
        for i in Classes.ITEmployee.itEmployeeList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                    """))
        choice -= 1
        teacherName = Classes.ITEmployee.itEmployeeList[choice].Classes.ITEmployee.return_employee()

        os.system('cls')
        choice = int(input("""Dodawanie grupy przedmiotowej.
                    Wybierz 1 aby studentów dziennych do grupy.
                    Wybierz 2 aby studentów zaocznych do grupy
                    """))
        if choice == "1":
            os.system('cls')
            studentNames = []
            studentNames = add_daily_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append(Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Dzienne", teacherName, studentNames))

        if choice == "2":
            os.system('cls')
            studentNames = []
            studentNames = add_weekend_student_to_group()
            Classes.SubjectGroups.subjectGroupsList.append( Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Zaoczne", teacherName, studentNames))
    else:
        os.system('cls')
        print("W bazie nie ma żadnych informatyków. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()
    if choice == "2":
        if not Classes.MathEmployee.mathEmployeeList:
            j = 1
            for i in Classes.MathEmployee.mathEmployeeList:
                print(j, '. ', i)
                j += 1
            choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                        """))
            choice -= 1
            teacherName = Classes.MathEmployee.mathEmployeeList[choice].Classes.MathEmployee.return_employee()

            os.system('cls')
            choice = int(input("""Dodawanie grupy przedmiotowej.
                        Wybierz 1 aby studentów dziennych do grupy.
                        Wybierz 2 aby studentów zaocznych do grupy
                        """))
            if choice == "1":
                os.system('cls')
                studentNames = []
                studentNames = add_daily_student_to_group()
                Classes.SubjectGroups.subjectGroupsList.append(
                    Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Dzienne", teacherName,
                                          studentNames))

            if choice == "2":
                os.system('cls')
                studentNames = []
                studentNames = add_weekend_student_to_group()
                Classes.SubjectGroups.subjectGroupsList.append(
                    Classes.SubjectGroups(subjectGroupName, subjectGroupID, "Zaoczne", teacherName,
                                          studentNames))
        else:
            os.system('cls')
            print("W bazie nie ma żadnych informatyków. Dodaj ich, i spróbuj ponownie.")
            subject_groups_menu()


    os.system('cls')
    print("Pomyślnie dodano studenta")
    print()
    add_subject_group()


def add_daily_student_to_group():
    if not Classes.DailyStudent.dailyStudentList:
        j = 1
        for i in Classes.DailyStudent.dailyStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                    """))
        choice -= 1
        studentNames = []
        studentNames.append(Classes.DailyStudent.dailyStudentList[choice].Classes.DailyStudent.return_student())
        choice=int(input("""
        Wybierz 1 aby dodać kolejnego studenta.
        Wybierz 0 aby powrócić"""))
        if choice == "1":
            add_daily_student_to_group()
        else:
            return studentNames

    else:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()


def add_weekend_student_to_group():
    if not Classes.WeekendStudent.weekendStudentList:
        j = 1
        for i in Classes.WeekendStudent.weekendStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pracownika którego chcesz dodać do grupy
                       """))
        choice -= 1
        studentNames = []
        studentNames.append(Classes.WeekendStudent.weekendStudentList[choice].Classes.WeekendStuden.return_student())
        choice = int(input("""
           Wybierz 1 aby dodać kolejnego studenta.
           Wybierz 0 aby powrócić"""))
        if choice == "1":
            add_daily_student_to_group()
        else:
            return studentNames

    else:
        os.system('cls')
        print("W bazie nie ma żadnych studentów dziennych. Dodaj ich, i spróbuj ponownie.")
        subject_groups_menu()


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
