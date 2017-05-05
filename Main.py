import os
import Classes


def start():
    choice=input(""" Witaj w aplikacji dziekanat.
    Wybierz 1 aby edytować informacje.
    Wybierz 2 aby wyświetlić bazę.
    Wybierz 3 aby wyświetlić statystyki.
    Wybierz 0 aby wyjść.
    """)

    if choice == "0":
        exit(0)
    if choice == "1":
        os.system('cls')
        edit_information_menu()
    if choice == "2":
        print("kappa")
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        start()


def edit_information_menu():
    choice = input(""" Edycja informacji.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby edytować informacje o studentach.
        Wybierz 2 aby edytować informacje o pracownikach.
        Wybierz 3 aby edytować informacje o przedmiotach.
        """)
    if choice == "0":
        os.system('cls')
        start()
    if choice == "1":
        os.system('cls')
        students_menu()
    if choice == "2":
        os.system('cls')
        employee_menu()
    if choice == "3":
        os.system('cls')
        subjects_menu()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        edit_information_menu()


def employee_menu():
    choice = input("""Pracownicy.
        Wybierz 0 aby powrócić do poprzedniego menu.
        Wybierz 1 aby dodać pracownika.
        Wybierz 2 aby usunąć pracownika.
        """)
    if choice == "0":
        employee_write_to_file()
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_employee()
    if choice == "2":
        os.system('cls')
        delete_employee()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
        """)
        employee_menu()


def employee_write_to_file():
    employees = open("pracownicy.txt", "w")
    for i in Classes.ITEmployee.itEmployeeList:
        employees.write(str(i)+'\n')
    for i in Classes.MathEmployee.mathEmployeeList:
        employees.write(str(i)+'\n')
        employees.close()


def add_employee():
    choice = input("""Dodawanie pracownika.

        Jeśli chcesz dodać informatyka wybierz 1. 
        Jeśli chcesz dodać matematyka wybierz 2. 
        Jeśli nie chcesz dodawać pracownika, wybierz 0.
        """)

    if choice == "0":
        os.system('cls')
        employee_menu()

    if choice == "1":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        salary = input("Podaj wynagrodzenie: ")
        Classes.ITEmployee.itEmployeeList.append(Classes.ITEmployee(name, surname, pesel, salary))
        os.system('cls')
        print("""Pomyślnie dodano pracownika
        """)
        add_employee()
    if choice == "2":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        salary = input("Podaj wynagrodzenie: ")
        Classes.MathEmployee.mathEmployeeList.append(Classes.MathEmployee(name, surname, pesel, salary))
        os.system('cls')
        print("Pomyślnie dodano pracownika")
        print()
        add_employee()

    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        add_employee()


def delete_employee():
    choice = input("""Usuwanie pracownika.
        Jeśli chcesz informatyka, wybierz 1.
        Jesli chcesz matematyka, wybierz 2.
        Jeśli chcesz powrócić do poprzedniego menu, wybierz 0.
        """)

    if choice == "0":
        os.system('cls')
        employee_menu()
    if choice == "1":
        os.system('cls')
        delete_it_employee()
    if choice == "2":
        os.system('cls')
        delete_math_employee()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        delete_employee()


def delete_it_employee():

    try:
        j = 1
        print("Usuwanie informatyka")
        print()
        if not Classes.ITEmployee.itEmployeeList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_employee()

        for i in Classes.ITEmployee.itEmployeeList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.ITEmployee.itEmployeeList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto informatyka.")
        print()
        delete_employee()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_daily_student()


def delete_math_employee():
    try:
        j = 1
        print("Usuwanie matematyka")
        print()
        if not Classes.MathEmployee.mathEmployeeList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_employee()

        for i in Classes.MathEmployee.mathEmployeeList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.MathEmployee.mathEmployeeList.pop(choice)
        os.system('cls')
        print("Pomyślnie matematyka.")
        print()
        delete_student()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_math_employee()


def students_menu():
    choice=input("""Studenci.
    Wybierz 0 aby powrócić do poprzedniego menu.
    Wybierz 1 aby dodać studenta.
    Wybierz 2 aby usunąć studenta.
    """)
    if choice == "0":
        students_write_to_file()
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        add_student()
    if choice == "2":
        os.system('cls')
        delete_student()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        students_menu()


def students_write_to_file():
    students = open("studenci.txt", "w")
    for i in Classes.DailyStudent.dailyStudentList:
        students.write(str(i)+'\n')
    for i in Classes.WeekendStudent.weekendStudentList:
        students.write(str(i)+'\n')
    students.close()


def add_student():
    choice = input("""Dodawanie studenta.
    
    Jeśli chcesz dodać studenta studiującego w trybie dziennym wybierz 1. 
    Jeśli chcesz dodać studenta studiującego w trybie zaocznym - wybierz 2. 
    Jeśli nie chcesz dodawać studenta, wybierz 0.
    """)

    if choice == "0":
        os.system('cls')
        students_menu()

    if choice == "1":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        studentID = input("Podaj numer indeksu: ")
        Classes.DailyStudent.dailyStudentList.append(Classes.DailyStudent(name, surname, pesel, studentID))
        os.system('cls')
        print("Pomyślnie dodano studenta")
        print()
        add_student()

    if choice == "2":
        os.system('cls')
        name = input("Podaj imię:")
        surname = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        studentID = input("Podaj numer indeksu: ")
        Classes.WeekendStudent.weekendStudentList.append(Classes.WeekendStudent(name, surname, pesel, studentID))
        os.system('cls')
        print("Pomyślnie dodano studenta")
        print()
        add_student()

    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        add_student()


def delete_student():

    choice = input("""Usuwanie studenta.
    Jeśli chcesz usunąć studenta dziennego, wybierz 1.
    Jesli chcesz usunąć studenta zaocznego, wybierz 2.
    Jeśli chcesz powrócić do poprzedniego menu, wybierz 0.
    """)

    if choice == "0":
        os.system('cls')
        students_menu()
    if choice == "1":
        os.system('cls')
        delete_daily_student()
    if choice == "2":
        os.system('cls')
        delete_weekend_student()
    else:
        os.system('cls')
        print("Wybrałeś złą wartość. Spróbuj ponownie.")
        print()
        delete_student()


def delete_daily_student():
    try:
        j = 1
        print("Usuwanie studenta dziennego")
        print()
        if not Classes.DailyStudent.dailyStudentList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_student()

        for i in Classes.DailyStudent.dailyStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.DailyStudent.dailyStudentList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto studenta.")
        print()
        delete_student()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_daily_student()


def delete_weekend_student():
    try:
        j = 1
        print("Usuwanie studenta zaocznego")
        print()
        if not Classes.WeekendStudent.weekendStudentList:
            print("Nic tu nie ma!")
            choice = input("""Wybierz cokolwiek aby powrócić.
            """)
            os.system('cls')
            delete_student()

        for i in Classes.WeekendStudent.weekendStudentList:
            print(j, '. ', i)
            j += 1
        choice = int(input("""Wybierz pozycję którą chcesz usunąć.
        """))
        choice -= 1  # ponieważ liczymy od 0 a nie od 1
        Classes.WeekendStudent.weekendStudentList.pop(choice)
        os.system('cls')
        print("Pomyślnie usunięto studenta.")
        print()
        delete_student()

    except:
        os.system('cls')
        print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
        """)
        delete_weekend_student()


def subjects_menu():
    choice = input("""Przedmioty.
            Wybierz 0 aby powrócić do poprzedniego menu.
            Wybierz 1 aby dodać przedmiot.
            Wybierz 2 aby usunąć przedmiot.
            """)
    if choice == "0":
        subject_write_to_file()
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        subjectName = input("Podaj nazwe przedmiotu:")
        subjectID = input("Podaj oznaczenie przedmiotu: ")
        Classes.Subjects.subjectList.append(Classes.Subjects(subjectName, subjectID))
        os.system('cls')
        print("Pomyślnie dodano przedmiot")
        print()
        subjects_menu()
    if choice == "2":
        os.system('cls')
        try:
            j = 1
            print("Usuwanie przedmiotu.")
            print()
            if not Classes.Subjects.subjectList:
                print("Nic tu nie ma!")
                choice = input("""Wybierz cokolwiek aby powrócić.
                """)
                os.system('cls')
                subjects_menu()

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
            subjects_menu()
        except:
            os.system('cls')
            print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
            """)
            subjects_menu()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
            """)
        subjects_menu()


def subject_write_to_file():
    subjects = open("przedmioty.txt", "w")
    for i in Classes.Subjects.subjectList:
        subjects.write(str(i) + '\n')
    subjects.close()


def subject_groups():
    choice = input("""Grupy przediotowe.
                Wybierz 0 aby powrócić do poprzedniego menu.
                Wybierz 1 aby dodać grupe przedmiotową.
                Wybierz 2 aby usunąć grupę przedmiotową.
                """)
    if choice == "0":
        subject_group_write_to_file()
        os.system('cls')
        edit_information_menu()
    if choice == "1":
        os.system('cls')
        subjectGroupName = input("Podaj nazwe przedmiotu:")
        studiesType = input("Podaj rodzaj studiów: ")
        subjectGroupID = input("Podaj oznaczenie grupy")
        teacherName = input ("Imię i nazwisko nauczyciela")
        nameOfStudents = input("Wprowadź imiona studentów")
        Classes.Subjects.subjectList.append(Classes.Subjects(subjectName, subjectID))
        os.system('cls')
        print("Pomyślnie dodano przedmiot")
        print()
        subjects_menu()
    if choice == "2":
        os.system('cls')
        try:
            j = 1
            print("Usuwanie przedmiotu.")
            print()
            if not Classes.Subjects.subjectList:
                print("Nic tu nie ma!")
                choice = input("""Wybierz cokolwiek aby powrócić.
                    """)
                os.system('cls')
                subjects_menu()

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
            subjects_menu()
        except:
            os.system('cls')
            print("""Wybrałeś nieprawidłową wartość. spróbuj ponownie
                """)
            subjects_menu()
    else:
        os.system('cls')
        print("""Wybrałeś złą wartość. Spróbuj ponownie.
                """)
        subjects_menu()




start()
