import Classes

import os


def students_menu():
    choice = input("""Studenci.
    Wybierz 0 aby powrócić do poprzedniego menu.
    Wybierz 1 aby dodać studenta.
    Wybierz 2 aby usunąć studenta.
    """)
    if choice == "0":
        students_write_to_file()
        os.system('cls')
        import Main
        Main.edit_information_menu()
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
        students.write(str(i) + '\n')
    for i in Classes.WeekendStudent.weekendStudentList:
        students.write(str(i) + '\n')
    students.close()


def show_students():
    for i in Classes.DailyStudent.dailyStudentList:
        print(i)
    for i in Classes.WeekendStudent.weekendStudentList:
        print(i)
    choice = int(input("""Wybierz 0 aby powrócić do poprzedniego menu.
    """))
    if choice == 0:
        import Main
        Main.show_base_menu()
    else:
        print("")

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